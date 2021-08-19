n = int(input(''))
group = []
table = []
for i in range(n):
    (size, money) = list(map(int, input('').split()))
    group += [(money, size, i)]
k = int(input(''))
out = []
all_money = 0
table = list(map(int, input('').split()))
for (money, size, j) in reversed(sorted(group)):
    max = 1000
    uu = -1
    for (i, table1) in enumerate(table):
        if size <= table1 < max + 1:
            max = table1
            uu = i
    if uu > -1:
        table[uu] = 0
        out += [(j, uu)]
        all_money += money
print(len(out), all_money)
for (i, j) in out:
    print(i + 1, j + 1)
