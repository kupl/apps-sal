class Solution:
    def uniqueLetterString(self, s: str) -> int:
        mod = 1000000007
    
        n = len(s)

        char_locs = defaultdict(list)
        for i in range(n):
            c = s[i]
            if not char_locs[c]: char_locs[c].append(-1)
            char_locs[c].append(i)


        ans = 0  
        for c in char_locs:
            char_locs[c].append(n)
            indices = char_locs[c]

            for i in range(1, len(indices)-1):
                before = indices[i] - indices[i-1]
                after = indices[i+1] - indices[i]

                ans = (ans + before*after) % mod

        return ans
