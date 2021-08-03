class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        all_sets = dsu(max(A))

        for element in A:
            for factor in range(2, int(sqrt(element)) + 1):
                if element % factor == 0:
                    all_sets.union(element, factor)
                    all_sets.union(element, element // factor)

        result = 0
        count = defaultdict(int)
        for element in A:
            parent_id = all_sets.find(element)
            count[parent_id] += 1
            result = max(result, count[parent_id])
        return result


class dsu:
    def __init__(self, size):
        self.parent = [x for x in range(size + 1)]
        self.size = [1 for x in range(size + 1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        index_x = self.find(x)
        index_y = self.find(y)

        if index_x == index_y:
            return index_x

        if self.size[index_x] > self.size[index_y]:
            index_x, index_y = index_y, index_x
        self.parent[index_x] = index_y
        self.size[index_y] += self.size[index_x]
        return index_y
