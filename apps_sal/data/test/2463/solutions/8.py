n = int(input())
l = list(map(int, input().split()))
l.sort()
duze = 0
male = 0
print((n - 1) // 2)
odp = []
for i in range(n):
    if i % 2 == 0:
        odp.append(l[n - 1 - duze])
        duze += 1
    else:
        odp.append(l[male])
        male += 1
print(*odp)
