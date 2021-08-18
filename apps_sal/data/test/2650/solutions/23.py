import heapq
import sys
input = sys.stdin.readline


class HeapDict:
    def __init__(self):
        self.h = []
        self.d = {}

    def insert(self, x):
        if x not in self.d or self.d[x] == 0:
            heapq.heappush(self.h, x)
        self.d.setdefault(x, 0)
        self.d[x] += 1

    def erase(self, x):
        if x not in self.d or self.d[x] == 0:
            return
        else:
            self.d[x] -= 1

        while self.h:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break

    def get_min(self):
        return self.h[0]

    def pop(self):
        poped_val = self.h[0]
        self.erase(poped_val)
        return poped_val

    def exist(self, x):
        return (x in self.d and self.d[x] > 0)

    def show_h(self):
        elems = [v for v in self.h if self.d[v] > 0]
        print(elems)

    def show_d(self):
        print(self.d)


def main():
    n, q = map(int, input().split())
    kid_rates = [0] * (n + 1)
    kid_kinders = [0] * (n + 1)
    kinder_kid_rates = [HeapDict() for _ in range(2 * (10**5) + 1)]
    for i in range(n):
        ind = i + 1
        a, b = map(int, input().split())
        kid_rates[ind] = a
        kid_kinders[ind] = b
        kinder_kid_rates[b].insert((a * (-1), ind))

    each_kinder_rate_maxs = HeapDict()
    for i, kkr in enumerate(kinder_kid_rates):
        if kkr.h:
            kkr_max = kkr.get_min()
            each_kinder_rate_maxs.insert((kkr_max[0] * (-1), kkr_max[1], i))

    cdl = []
    for _ in range(q):
        c, d = map(int, input().split())
        cdl.append((c, d))

    for cd in cdl:
        c, d = cd
        to_kinder = d
        kid_rate = kid_rates[c]
        from_kinder = kid_kinders[c]

        from_kinder_max_rate = kinder_kid_rates[from_kinder].get_min()
        each_kinder_rate_maxs.erase((from_kinder_max_rate[0] * (-1), from_kinder_max_rate[1], from_kinder))

        kinder_kid_rates[from_kinder].erase((kid_rate * (-1), c))

        if kinder_kid_rates[from_kinder].h:
            new_max_rate = kinder_kid_rates[from_kinder].get_min()
            each_kinder_rate_maxs.insert((new_max_rate[0] * (-1), new_max_rate[1], from_kinder))

        if kinder_kid_rates[to_kinder].h:
            to_kinder_max_rate = kinder_kid_rates[to_kinder].get_min()
            each_kinder_rate_maxs.erase((to_kinder_max_rate[0] * (-1), to_kinder_max_rate[1], to_kinder))

        kinder_kid_rates[to_kinder].insert((kid_rate * (-1), c))
        new_to_kinder_max_rate = kinder_kid_rates[to_kinder].get_min()
        each_kinder_rate_maxs.insert((new_to_kinder_max_rate[0] * (-1), new_to_kinder_max_rate[1], to_kinder))

        print(each_kinder_rate_maxs.get_min()[0])
        kid_kinders[c] = to_kinder


def __starting_point():
    main()


__starting_point()
