class Solution(object):
    def subarrayBitwiseORs(self, A):
        final = set()
        actual = set()
        for el in A:
            actual = {el} | {el2 | el for el2 in actual}
            final |= actual
        return len(final)
