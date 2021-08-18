def pairs(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            yield (arr[i], arr[j])


def count(A, B):

    tally_A = {}
    for elem in A:
        tally_A.setdefault(elem ** 2, 0)
        tally_A[elem ** 2] += 1

    tally_B = {}
    for e, f in pairs(B):
        tally_B.setdefault(e * f, 0)
        tally_B[e * f] += 1

    return sum(tally_A[e] * tally_B[e] for e in tally_A if e in tally_B)


class Solution:
    def numTriplets(self, A: List[int], B: List[int]) -> int:
        return count(A, B) + count(B, A)
