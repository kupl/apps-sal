import heapq


class HeapDict:
    def __init__(self):
        # heapqとdictを用意
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
            print((x, "is not in HeapDict"))
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
    N, Q = list(map(int, input().split()))
    A = []  # レート
    B = []  # 所属幼稚園
    con = 2 * 10 ** 5
    INF = 10 ** 18
    youchi = [HeapDict() for _ in range(con)]  # 各幼稚園に対するHeapDict
    max_values = HeapDict()  # 各幼稚園の最大値のHeapDict
    for i in range(N):
        a, b = list(map(int, input().split()))
        b -= 1
        A.append(a)
        B.append(b)
        youchi[b].insert(-a)

    for i in range(con):  # 各幼稚園の最大値をまとめる
        if youchi[i].size() != 0:
            max_values.insert(-youchi[i].get_min())

    for i in range(Q):
        c, d = list(map(int, input().split()))
        c -= 1
        d -= 1
        rate = A[c]
        youchi_now = B[c]
        youchi_next = d

        # 最強園児のレートの集合から、転園する園児の元の幼稚園の元の最強園児のレートを、削除する
        max_values.erase(-youchi[youchi_now].get_min())

        # 転園する園児の元の幼稚園のレートの集合から、転園する園児のレートを、削除する
        youchi[youchi_now].erase(-rate)

        # 最強園児のレートの集合に、転園する園児の元の幼稚園の新しい最強園児のレートを、挿入する(園児が一人もいない場合何もしない)
        if youchi[youchi_now].size() != 0:
            max_values.insert(-youchi[youchi_now].get_min())

        # 最強園児のレートの集合から、転園する園児の新しい幼稚園の元の最強園児のレートを、削除する(園児が一人もいない場合何もしない)
        if youchi[youchi_next].size() != 0:
            max_values.erase(-youchi[youchi_next].get_min())

        # 転園する園児の新しい幼稚園のレートの集合に、転園する園児のレートを、挿入する
        youchi[youchi_next].insert(-rate)

        # 最強園児のレートの集合に、転園する園児の新しい幼稚園の新しい最強園児のレートを、挿入する
        max_values.insert(-youchi[youchi_next].get_min())

        # 転園する園児の所属する幼稚園の番号を更新する
        B[c] = youchi_next

        print((max_values.get_min()))


def __starting_point():
    main()


__starting_point()
