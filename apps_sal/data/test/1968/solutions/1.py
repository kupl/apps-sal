(n, m) = map(int, input().split())
s = 0
q = []
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(1, a[0] + 1):
        if m > a[j]:
            s += 1
            q.append(i + 1)
            break
print(s)
print(*q)
