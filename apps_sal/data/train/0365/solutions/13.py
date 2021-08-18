class Solution:
    def uniqueLetterString(self, s: str) -> int:

        last = collections.defaultdict(int)
        count = 0
        for i, char in enumerate(s):
            for comp in last:
                if comp != char:
                    count += last[comp][1]
                else:
                    count += i - last[comp][0]
                    last[char] = (i, i - last[comp][0])
            if char not in last:
                count += i + 1
                last[char] = (i, i + 1)
        return count
