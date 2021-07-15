class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        ## https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/463921/python-backtracking-with-pruning-tricks
        ## from low digit position to high digit position, stop searching once (left side sum)%10 did not equal right side at current digit
        
        ## mark all initial characters, because not leading zeros are allowed. 
        start = set()
        for word in words + [result]:
            if len(word) > 1: ## note: a single 0 is allowed
                start.add(word[0])

        ## find the maximum length between all words and result
        n = max(list(map(len, words + [result])))
        if len(result) < n: ## if the length of result is shorter than other words, it's  not possible
            return False
        
        ## helper function:
        ## idx: the index currently processing (of words and result)
        ## i: i-th word in words; when i == len(words) + 1: we have processed all words + result at index 
        ## carry: the carry computed by summing all previous indexes of words
        def dfs(idx, i, carry, visited, mp):
            ## base case: when we reach the highest digit (most significant) position
            ## we should have carry == 0, otherwise the sums are not equal
            if idx == n: 
                return carry == 0
            ## when i == len(words) + 1: we have processed all words + result at index
            ## the specific index of word is word[-idx - 1]
            ## we check the sum added by carry
            ## if the sum does not match the digit at result[-idx - 1]
            ## return False
            if i == len(words) + 1:
                sums = sum(mp[word[-idx - 1]] if idx < len(word) else 0 for word in words) + carry
                if sums % 10 == mp[result[-idx - 1]]:
                    carry = sums // 10 ## update carry to the next index
                    ## recursive call to the next index and start from 0-th word
                    return dfs(idx + 1, 0, carry, visited, mp)
                return False 
            ## if current word (i-th) has shorter length than index, 
            ## skip it, it will be counted as 0 for this digit
            if (i < len(words) and idx >= len(words[i])):
                return dfs(idx, i + 1, carry, visited, mp)
            
            
            tmp = words + [result]
            ch = tmp[i][-idx-1] ## current character
            if ch in mp: ## if this character has been assigned a value
                return dfs(idx, i + 1, carry, visited, mp)
            
            ## backtrack: try every possible digit
            begin = 0
            if ch in start:
                begin = 1 ## if it is an initial character of some word
            for x in range(begin, 10):
                if x not in visited:
                    visited.add(x)
                    mp[ch] = x
                    if dfs(idx, i + 1, carry, visited, mp.copy()):
                        return True
                    visited.remove(x)
            return False
        return dfs(0, 0, 0, set(), {})
            
        

