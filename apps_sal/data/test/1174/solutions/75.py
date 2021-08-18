class Heap:
    """
    練習用に書いたクラス
    本番は'heapq'を使う
    """

    def __init__(self, x: list):
        self.heap = []
        for item in x:
            self.push(item)

    def push(self, item: int):
        self.heap.append(item)
        idx_child = len(self.heap) - 1
        while (idx_child > 0):
            idx_parent = (idx_child - 1) // 2
            if self.heap[idx_parent] <= item:
                break
            tmp = self.heap[idx_child]
            self.heap[idx_parent], self.heap[idx_child] \
                = self.heap[idx_child], self.heap[idx_parent]
            idx_child = idx_parent

    def pop(self) -> int:
        ret = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        idx_parent = 0
        while (idx_parent * 2 + 1 < len(self.heap)):
            idx_child_l, idx_child_r = 2 * idx_parent + 1, 2 * idx_parent + 2
            if idx_child_r < len(self.heap) and self.heap[idx_child_r] < self.heap[idx_child_l]:
                idx_child = idx_child_r
            else:
                idx_child = idx_child_l
            if self.heap[idx_parent] <= self.heap[idx_child]:
                break
            self.heap[idx_child], self.heap[idx_parent] \
                = self.heap[idx_parent], self.heap[idx_child]
            idx_parent = idx_child
        return ret

    def load(self) -> list:
        return self.heap


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [-a for a in A]
heap = Heap(A)
for _ in range(M):
    x = heap.pop()
    heap.push(x / 2)
A = heap.load()
A = [int(-a) for a in A]
print(sum(A))
