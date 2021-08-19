class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        collections = {}
        for (i, el) in enumerate(A):
            if el in collections:
                collections[el][1] = i
            else:
                collections[el] = [i, i]
        sorted_collections = sorted(collections.keys())
        for i in range(1, len(sorted_collections)):
            (left, right) = (i, len(sorted_collections) - i - 1)
            collections[sorted_collections[left]][0] = min(collections[sorted_collections[left]][0], collections[sorted_collections[left - 1]][0])
            collections[sorted_collections[right]][1] = max(collections[sorted_collections[right]][1], collections[sorted_collections[right + 1]][1])
        result = 0
        for el in collections.values():
            result = max(result, el[1] - el[0])
        return result
