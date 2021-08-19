n = int(input())
lst = list(map(int, input().split()))
perm = [0]
x = 0
for i in lst:
    perm.append(perm[x] + i)
    x += 1
k = 1 - min(perm)
for i in range(n):
    perm[i] += k
s_perm = sorted(perm)
k = 1
for i in s_perm:
    if i != k:
        print(-1)
        quit()
    k += 1
print(*perm)
