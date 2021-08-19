"""
Start: 2:25 p.m.
"""
'\n- Visualize everything.\n- Work with concrete examples.\n- Commit to a hunch. Crystallize it into an approach that can be evaluated (validated/invalidated). OK if approach seems unlikely to work.\n'
'\n[16, 16]\n\nA will not send FR to someone who is older (same age OK).\n=> sort the array\n\nA will not send FR to someone who is "much" younger.\nIf A is under 100, he will not send FR to anyone over 100.\nNot FR self.\n'
'\nBrute-force: evaluate every pair\nTime: O(n^2)\nSpace: O(1)\n'
'\n- A will not friend anyone older so no need to look forward, only backward.\n\nTime:O(n log n)\nSpace: O(n)\n\n- Sort\n- For each num, compute minimum bound, BS.\n\nlb = 16/8 + 7 = 15\n\n[16,17,18]\n i\n \n 17/2 = 8.5 ~= 8\n 15\n'
'\nTest Cases\nno numbers before i (works)\n[5]\n i\n \n nothing >= lower bound (works)\n [1, 2, 50]\n        i\n        \nlb = 32\nmultiple occurrences of lb (works)\n[1, 2, 32, 32, 40, 41, 50]\n       m\n l\n       r\n                       i\n       ret\n               \nlb = 32\nonly > lb (works)\n[1, 2, 40, 41, 50] \n               i\n       ret\n       \n[40, 41, 50] (works)\n         i\n ret\n'
'\nPASS\n[1, 2, 32, 32, 40, 41, 50]\n[1, 2, 50]\n[1, 2, 40, 41, 50] \n[40, 41, 50]\n[16,16]\n'


class Solution:

    def firstLTE(self, lowerBound, ages, endIndex):
        if endIndex < 0:
            return 0
        l = 0
        r = endIndex
        while l < r:
            m = (l + r) // 2
            if ages[m] <= lowerBound:
                l = m + 1
            else:
                r = m
        if l <= r and ages[l] > lowerBound:
            return l
        return endIndex + 1

    def findEarliest(self, key, ages, endIndex):
        if endIndex < 0:
            return -1
        l = 0
        r = endIndex
        while l < r:
            m = (l + r) // 2
            if ages[m] >= key:
                r = m
            else:
                l = m + 1
        if l <= endIndex and ages[l] == key:
            return l
        return -1
    '\n    [16, 16]\n     l\n     r\n         i\n      \n     lowerBound = 23\n    [1, 2, 32, 32]\n        m        \n           l\n           r\n    '

    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0
        numRequests = 0
        ages.sort()
        for (i, a) in enumerate(ages):
            lowerBound = a * 0.5 + 7
            startIndex = self.firstLTE(lowerBound, ages, i - 1)
            numRequests += i - startIndex
            if a > lowerBound:
                startIndex = self.findEarliest(a, ages, i - 1)
                if startIndex >= 0 and startIndex < i:
                    numRequests += i - startIndex
        return numRequests


'\n[73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]\n'
