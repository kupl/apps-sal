n, m = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
a = [0] * n

used = [0] * (n + 1)
cnt = 0

for i in range(len(l) - 1):
    z = l[i + 1] - l[i]
    if z <= 0:
        z += n
    if used[z] and a[l[i] - 1] != z:
        print(-1)
        return
    a[l[i] - 1] = z
    used[z] = 1

j = 1
for i in range(len(a)):
    if a[i] == 0:
        while used[j]:
            j += 1
            if j > n:
                print(-1)
                return
        a[i] = j
        used[j] = 1

if all(a) and all(used[1:]):
    print(*a)
else:
    print(-1)
