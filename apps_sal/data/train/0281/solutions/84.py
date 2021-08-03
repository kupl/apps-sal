class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        valid = {}
        moves = []
        for a, b in zip(s, t):
            if a != b:
                diff = ord(b) - ord(a)
                if diff < 0:
                    diff += 26
                if diff in valid:
                    valid[diff].append(valid[diff][-1] + 26)
                else:
                    valid.setdefault(diff, [diff])
                moves.append(diff)
        for d in moves:
            num = valid[d]
            if num[-1] > k:
                return False
            else:
                num.pop()
        return True
