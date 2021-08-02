n = int(input())
a = sorted(map(int, input().split()))
l = [0] * (10**6 + 1)
M = max(a)

for i in a:
    if l[i] == 0:
        l[i] = 1
        for j in range(i * 2, M + 1, i):
            l[j] = -1
    else:
        l[i] = -1
print(l.count(1))
