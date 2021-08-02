I = [int(i) for i in input().split()]
n, m, pl, s = I[0], I[1], [], 0
for i in range(n):
    I = [int(i) for i in input().split()]
    s += I[0] * I[1]
    pl.append(s)
M = [int(i) for i in input().split()]
index = 0
for i in M:
    for j in range(index, n):
        if i <= pl[j]:
            print(j + 1)
            index = j
            break
