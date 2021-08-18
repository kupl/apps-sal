import heapq
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    syozoku = [0] * (n + 1)
    rate = [0] * (n + 1)
    enrate = [0] * (2 * 10**5 + 1)
    saikyourate = HeapDict()
    for i in range(1, 2 * 10**5 + 1):
        enrate[i] = HeapDict()
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        syozoku[i] = b
        rate[i] = a
        enrate[b].insert(-a)
    for i in range(1, 2 * 10**5 + 1):
        if len(enrate[i].h) != 0:
            saikyourate.insert(-(enrate[i].get_min()))
    for _ in range(q):
        c, d = map(int, input().split())
        saikyourate.erase(-(enrate[syozoku[c]].get_min()))
        enrate[syozoku[c]].erase(-rate[c])
        if len(enrate[syozoku[c]].h) != 0:
            saikyourate.insert(-(enrate[syozoku[c]].get_min()))
        if len(enrate[d].h) != 0:
            saikyourate.erase(-(enrate[d].get_min()))
        enrate[d].insert(-rate[c])
        saikyourate.insert(-(enrate[d].get_min()))
        syozoku[c] = d
        print(saikyourate.get_min())


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
            print(x, "is not in HeapDict")
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
            return False

    def get_min(self):
        return self.h[0]


def __starting_point():
    main()


__starting_point()
