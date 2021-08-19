import heapq


class HeapDict:

    def __init__(self):
        self.h = []
        self.d = dict()

    def insert(self, x):
        heapq.heappush(self.h, x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self, x):
        if x not in self.d or self.d[x] == 0:
            print((x, 'is not in HeapDict'))
            return
        else:
            self.d[x] -= 1
        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self, x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            False

    def get_min(self):
        return self.h[0]

    def size(self):
        return len(self.h)


def main():
    (N, Q) = list(map(int, input().split()))
    A = []
    B = []
    con = 2 * 10 ** 5
    INF = 10 ** 18
    youchi = [HeapDict() for _ in range(con)]
    max_values = HeapDict()
    for i in range(N):
        (a, b) = list(map(int, input().split()))
        b -= 1
        A.append(a)
        B.append(b)
        youchi[b].insert(-a)
    for i in range(con):
        if youchi[i].size() != 0:
            max_values.insert(-youchi[i].get_min())
    for i in range(Q):
        (c, d) = list(map(int, input().split()))
        c -= 1
        d -= 1
        rate = A[c]
        youchi_now = B[c]
        youchi_next = d
        max_values.erase(-youchi[youchi_now].get_min())
        youchi[youchi_now].erase(-rate)
        if youchi[youchi_now].size() != 0:
            max_values.insert(-youchi[youchi_now].get_min())
        if youchi[youchi_next].size() != 0:
            max_values.erase(-youchi[youchi_next].get_min())
        youchi[youchi_next].insert(-rate)
        max_values.insert(-youchi[youchi_next].get_min())
        B[c] = youchi_next
        print(max_values.get_min())


def __starting_point():
    main()


__starting_point()
