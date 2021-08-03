from collections import Counter


class Solution(object):
    def countTriplets(self, A):
        c = Counter(x & y for x in A for y in A)
        return sum(c[xy] for xy in c for z in A if xy & z == 0)
