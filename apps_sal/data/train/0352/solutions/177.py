class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        by_length = collections.defaultdict(set)
        for word in words:
            by_length[len(word)].add(word)

        longest = 1
        seen = {*()} # set()
        mx = len(by_length)
        mn = min(by_length)
        
        # in descending order
        for length in sorted(by_length, reverse=True):
            if length == mn: return 1
            if length - mn < longest:
                break
            for word in by_length[length]:
                if length - mn < longest:
                    break
                if word in seen:
                    continue
                stk = [(word, length, 1)]
                while stk:
                    word, k, n = stk.pop()
                    seen.add(word)
                    if n > longest:
                        longest = n
                    for i in range(k):
                        pre = word[:i] + word[i+1:]
                        if pre not in seen and pre in by_length[k-1]:
                            stk.append((pre, k-1, n+1))
                if longest == mx:
                    return longest

        return longest   
