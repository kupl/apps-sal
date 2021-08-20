def main():
    N = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    xor_a = [a[i] ^ a[(i + 1) % N] for i in range(len(a))]
    xor_b = [b[i] ^ b[(i + 1) % N] for i in range(len(b))]
    kmp = KmpSearch(xor_a + xor_a, xor_b)
    ans = kmp.full_search()
    for k in ans:
        if k == len(a):
            break
        print(str(k) + ' ' + str(a[0 + k] ^ b[0]))


class KmpSearch:

    def __init__(self, target, pattern):
        self.target = target
        self.pattern = pattern
        self.__table = self.__create_kmp_table()

    def full_search(self):
        if len(self.pattern) > len(self.target):
            return -1
        res = []
        i = 0
        p = 0
        while i < len(self.target):
            if self.pattern[p] == self.target[i]:
                i += 1
                p += 1
                if p == len(self.pattern):
                    res.append(i - p)
                    i -= 1
                    p = self.__table[p - 1]
            elif p == 0:
                i += 1
            else:
                p = self.__table[p]
        return res

    def __create_kmp_table(self):
        table = [0 for x in range(len(self.pattern))]
        j = 0
        for i in range(1, len(self.pattern)):
            table[i] = j
            if self.pattern[j] == self.pattern[i]:
                j += 1
            else:
                j = 0
        return table


def __starting_point():
    main()


__starting_point()
