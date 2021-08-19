n = int(input())
a = [int(x) for x in input().split()]
a.sort()
p = []
q = []
for i in range(n):
    if i % 2 == 0:
        p.append(a[i])
    else:
        q.append(a[i])
q.reverse()
ans = p + q
for i in ans:
    print(i, end=' ')
print()
