class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        prev = [[s[0]]]
        for elm in s[1:]:
            current = []
            for sub in prev:
                copy = list(sub)
                copy[-1] = copy[-1] + elm
                current.append(copy)

                copy = list(sub)
                copy.append(elm)
                current.append(copy)

            prev = current

        return max(len(set(combo)) for combo in prev)
