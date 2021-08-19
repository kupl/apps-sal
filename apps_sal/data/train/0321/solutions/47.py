class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = list()
        l2 = list()
        n = len(s1)
        # Make s1 into l1
        for i in range(0, n):
            l1.append(s1[i:i + 1])
        l1.sort()
        # Make s2 into l2
        for i in range(0, n):
            l2.append(s2[i:i + 1])
        l2.sort()
        # See if s1 can break s2
        indicator = False
        l1_test = list()
        for i in range(0, n):
            if l1[i] >= l2[i]:
                l1_test.append(1)
        if len(l1_test) == len(l1):
            indicator = True
        # See if s2 can break s1
        l2_test = list()
        for i in range(0, n):
            if l2[i] >= l1[i]:
                l2_test.append(1)
        if len(l2_test) == len(l2):
            indicator = True
        return indicator
