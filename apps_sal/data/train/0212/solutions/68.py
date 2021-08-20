MOD = 10 ** 9 + 7


def count_binary_trees(arr):
    arr = sorted(arr)
    coll = set(arr)
    count = {}
    for (index, elem) in enumerate(arr):
        ans = 1
        for i in range(index):
            factor = arr[i]
            if elem % factor == 0 and elem // factor in coll:
                other_factor = elem // factor
                ans = (ans + count[factor] * count[other_factor]) % MOD
        count[elem] = ans
    return sum((y for (x, y) in count.items())) % MOD


class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        return count_binary_trees(A)
