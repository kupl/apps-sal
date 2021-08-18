class UnionFind():
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] > self.table[s2]:
                self.table[s2] = s1
            elif self.table[s1] < self.table[s2]:
                self.table[s1] = s2
            else:
                self.table[s1] = s2
                self.table[s2] -= 1
        return


n = int(input())
d = [[] for _ in range(4)]
uf = UnionFind(4)
CVC = [list(map(int, input().split())) for _ in range(n)]
vals = []
min_not_auto = float("inf")
for i in range(n):
    cvc = CVC[i]
    vals.append(cvc[1])
    d[cvc[0] - 1].append(cvc[1])
    d[cvc[2] - 1].append(cvc[1])
    if cvc[0] != cvc[2] and cvc[1] < min_not_auto:
        min_not_auto = cvc[1]

    uf.union(cvc[0] - 1, cvc[2] - 1)

root_num = 0
for i in range(4):
    if uf.table[i] < 0:
        root_num += 1

if root_num == 1:
    odd = True
    for i in range(4):
        if len(d[i]) % 2 == 0:
            odd = False
            break
    if odd:
        print(sum(vals) - min_not_auto)
    else:
        answers = [0] * 4
        for i in range(4):
            answers[uf.find(i)] += sum(d[i])
        print(max(answers) // 2)

else:
    answers = [0] * 4
    for i in range(4):
        answers[uf.find(i)] += sum(d[i])
    print(max(answers) // 2)
