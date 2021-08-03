class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        if len(s) == 1:
            return 1

        ltrs = set(list(s))

        counts = {}
        for ltr in ltrs:
            counts[ltr] = s.count(ltr)

        unique_count = 0
        for ltr, count in list(counts.items()):
            if count == 1:
                index = s.index(ltr)
                if index == 0 or index == len(s) - 1:
                    s = s.replace(ltr, '')
                    unique_count = unique_count + 1
                else:
                    prev = s[index - 1]
                    next = s[index + 1]
                    if counts[prev] == 1 and counts[next] == 1:
                        s = s.replace(ltr, '')
                        unique_count = unique_count + 1

        if len(s) == 0:
            return unique_count
        else:
            return unique_count + self.find_max(len(s) - 1, s)

    def find_max(self, i, s):
        from sortedcontainers import SortedSet

        unique, unique_count = False, -1
        words = s.split()
        if len(words) == len(set(words)):
            unique_count = len(words)

        if i == 0:
            return unique_count

        a = self.find_max(i - 1, s[:i] + ' ' + s[i:])
        b = self.find_max(i - 1, s)

        return max(a, b, unique_count)
