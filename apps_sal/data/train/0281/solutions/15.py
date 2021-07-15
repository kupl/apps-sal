class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        shifts = []
        for ch1, ch2 in zip(s, t):
            asc1 = ord(ch1) - ord('a')
            asc2 = ord(ch2) - ord('a')
            diff = asc2 - asc1 if asc2 >= asc1 else 26 - asc1 + asc2
            assert diff >= 0
            if diff > 0:
                shifts.append(diff)
        
        shifts.sort()
    
        most = 0
        freq = defaultdict(int)
        for s in shifts:
            most = max(most, s + freq[s] * 26)
            freq[s] += 1
        return most <= k
