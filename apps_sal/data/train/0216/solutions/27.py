class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        res = croaking = c = r = o = a = k = 0
        for x in croakOfFrogs:
            if x == 'c':
                c, croaking = c+1, croaking+1
                res = max(res, croaking)
            elif x == 'r': r += 1
            elif x == 'o': o += 1
            elif x == 'a': a += 1
            else: k, croaking = k+1, croaking-1
            if c < r or r < o or o < a or a < k: return -1 
        
        return res if c == r == o == a == k and croaking == 0 else -1

