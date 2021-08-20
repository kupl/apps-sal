class Solution:

    def minNumberOfFrogs(self, s: str) -> int:
        rec = defaultdict(int)
        count = 0
        if not s.startswith('c') or not s.endswith('k'):
            return -1
        for i in range(len(s)):
            if rec['c'] >= rec['r'] >= rec['o'] >= rec['a'] >= rec['k']:
                rec[s[i]] += 1
                if count < rec['c']:
                    count += 1
                if s[i] == 'k':
                    for k in rec:
                        rec[k] -= 1
            else:
                return -1
        return count
