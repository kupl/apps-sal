class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1Sorted = sorted(s1)
        s2Sorted = sorted(s2)

        return all(char1 >= char2 for char1, char2 in zip(s1Sorted, s2Sorted)) or all(char1 <= char2 for char1, char2 in zip(s1Sorted, s2Sorted))
