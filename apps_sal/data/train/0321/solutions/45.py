class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        def ifbreaks(a, b):
            a = sorted(a)
            b = sorted(b)
            for i in range(len(a)):
                if a[i] < b[i]:
                    return False
            return True
        return ifbreaks(s1, s2) or ifbreaks(s2, s1)
