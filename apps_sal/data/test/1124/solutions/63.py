from heapq import heappush, heappop, heapify
class RemovableHeap:
    def __init__(self, is_max_heap: bool=False, data :list=None):
        self.data = [] if data is None else data
        self.erased = []
        self.sign = -1 if is_max_heap else 1
    
    def normalize(self):
        while self.erased and self.data[0] == self.erased[0]:
            heappop(self.data)
            heappop(self.erased)
    
    def pop(self):
        ret = self.sign * heappop(self.data)
        self.normalize()
        return ret

    def push(self, x):
        heappush(self.data, self.sign * x)
        self.normalize()
    
    def remove(self, x):
        heappush(self.erased, self.sign * x)
        self.normalize()
    
    def __len__(self):
        return max(len(self.data) - len(self.erased), 0)
    
    def get(self):
        return self.sign * self.data[0]
def main():
    N = int(input())
    A = set(map(int, input().split()))

    max_que = RemovableHeap(is_max_heap=True)
    min_que = RemovableHeap()
    for a in A:
        max_que.push(a)
        min_que.push(a)

    while min_que.get() != max_que.get():
        min_A = min_que.get()
        while min_A < max_que.get():
            X = max_que.pop()
            min_que.remove(X)
            max_que.push((X - 1) % min_A + 1)
            min_que.push((X - 1) % min_A + 1)
        max_que.remove(min_que.pop())


    print((max_que.get()))
main()


