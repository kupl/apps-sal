class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t) or len(s) == 0:
            return False

        dists = [(26 + ord(b) - ord(a)) % 26 for a, b in zip(s, t)]
        counter = Counter(dists)
        print((dists, counter))
        for i in range(1, 26):
            if counter[i] > (k - i) // 26 + 1:
                return False
        
        return True
            

