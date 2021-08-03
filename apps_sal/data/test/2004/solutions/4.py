def reader(contest):
    inp = input
    if not contest:
        fin = open("in", "r")
        def inp(): return fin.readline()[:-1]

    def read(): return tuple(map(int, inp().split()))
    return inp, read


inp, read = reader(True)

n = read()[0]

l1, l2 = [], []

for i in range(1, n, 2):
    l1 += [i + 1]
for i in range(0, n, 2):
    l2 += [i + 1]
for i in range(1, n, 2):
    l1 += [i + 1]

l1ld2 = len(l1) // 2
print(len(l1) + len(l2))
print(*(l1[:l1ld2] + l2 + l1[l1ld2:]))
