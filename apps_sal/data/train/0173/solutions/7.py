class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
                ## APPROACH : 2 SUM ##
        ## LOGIC ##
\t\t## 1. Store the remainders in the hashmap and check if the current number has remaining remainder available in the hashset ##
        freq {remainder: remainder count}
        return true if not any of the pairs are true => we check if the freq[k-x%k]!=freq[x%k]. If we find any of such instance to be true, we return false

        '''
        freq = collections.Counter(map(lambda x: x % k, arr))
        return not any(val % 2 if not key else val != freq[k - key] for key, val in freq.items())
