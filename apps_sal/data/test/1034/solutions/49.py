from heapq import heapify, heappop, heappush, heappushpop


class PriorityQueue:
    def __init__(self, heap):
        '''
        heap ... list
        '''
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)


x, y, z, k = list(map(int, input().split()))
a_ls = list(map(int, input().split()))
b_ls = list(map(int, input().split()))
c_ls = list(map(int, input().split()))

a_ls.sort()
a_ls.reverse()
b_ls.sort()
b_ls.reverse()
c_ls.sort()
c_ls.reverse()

heap = []

q = PriorityQueue(heap)
q.push((-(a_ls[0] + b_ls[0] + c_ls[0]), 0, 0, 0))
considered = set()
for i in range(k):
    val, i, j, k = q.pop()
    print((-val))
    for di, dj, dk in zip([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        ni = i + di
        nj = j + dj
        nk = k + dk
        if ni >= x or nj >= y or nk >= z:
            continue
        if (ni, nj, nk) not in considered:
            considered.add((ni, nj, nk))
            q.push((-(a_ls[ni] + b_ls[nj] + c_ls[nk]), ni, nj, nk))
