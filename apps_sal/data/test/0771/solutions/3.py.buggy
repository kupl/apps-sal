n, k, m = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
mi = [[] for i in range(m)]
for i in s:
    mi[i % m].append(i)
for i in range(m):
    if len(mi[i]) >= k:
        print("Yes")
        print(*mi[i][:k])
        return
        break
print("No")
