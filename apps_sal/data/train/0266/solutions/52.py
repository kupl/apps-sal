class Solution:
    def numSplits(self, s: str) -> int:
        left = Counter()
        right = Counter(s)
        res = 0
        for ch in s :
            if right[ch] == 1:
                del right[ch]
            else:
                right[ch] -= 1
            left[ch] += 1
            #print (right,left)
            if len(list(left.keys())) == len(list(right.keys())):
                res += 1
        return res
        

