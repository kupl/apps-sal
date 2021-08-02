n = int(input())
al = list(map(int, input().split()))

res = 0

al.append(0)
al.insert(0, 0)

for i in range(n + 1):
    res += abs(al[i + 1] - al[i])

for j in range(1, n + 1):
    if (al[j + 1] - al[j]) * (al[j] - al[j - 1]) >= 0:
        print(res)
    else:
        print(res - min(abs(al[j + 1] - al[j]), abs(al[j] - al[j - 1])) * 2)
