_ROOT = object()


class UnionSet:

    def __init__(self):
        self.parents = {}
        self.sizes = {}
        self.size_histogram = collections.defaultdict(int)

    def has_size(self, size):
        return self.size_histogram[size] != 0

    def add(self, x):
        self.parents[x] = _ROOT
        self.sizes[x] = 1
        self.size_histogram[1] += 1
        self.merge(x, x - 1)
        self.merge(x, x + 1)

    def root(self, x):
        path = []
        while self.parents[x] != _ROOT:
            path.append(x)
            x = self.parents[x]
        for y in path:
            self.parents[y] = x
        return x

    def merge(self, x, y):
        if y not in self.parents:
            return
        x = self.root(x)
        y = self.root(y)
        self.size_histogram[self.sizes[x]] -= 1
        self.size_histogram[self.sizes[y]] -= 1
        merged_size = self.sizes[x] + self.sizes[y]
        self.size_histogram[merged_size] += 1
        if self.sizes[x] < self.sizes[y]:
            del self.sizes[x]
            self.parents[x] = y
            self.sizes[y] = merged_size
        else:
            del self.sizes[y]
            self.parents[y] = x
            self.sizes[x] = merged_size


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        union_set = UnionSet()
        latest_step = -1
        for (step, pos) in enumerate(arr):
            union_set.add(pos)
            if union_set.has_size(m):
                latest_step = step + 1
        return latest_step
