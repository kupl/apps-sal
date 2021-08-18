import math


class Heap():

    def __init__(self, array):
        self.array = list(array)
        self._build_heap()

    def _build_heap(self):
        for i in reversed(range(len(self.array) // 2)):
            self._min_heap(i)

    def _min_heap(self, i):
        left = (2 * (i + 1)) - 1
        right = (2 * (i + 1) + 1) - 1
        length = len(self.array) - 1
        smallest = i

        if left <= length and self.array[i] > self.array[left]:
            smallest = left
        if right <= length and self.array[smallest] > self.array[right]:
            smallest = right
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self._min_heap(smallest)

    def pop(self):
        tmp = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self._min_heap(0)
        return tmp

    def push(self, v):
        self.array.append(v)
        index = len(self.array)
        while self.array[(index // 2) - 1] > self.array[index - 1]:
            self.array[(index // 2) - 1], self.array[index - 1] = self.array[index - 1], self.array[(index // 2) - 1]
            index = index // 2


n, m = map(int, input().split())
a = map(lambda x: int(x) * -1, input().split())

a = Heap(a)

for i in range(m):
    a.push(math.ceil(a.pop() / 2))

print(int(-1 * sum(a.array)))
