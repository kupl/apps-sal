n, k = list(map(int, input().split()))
p = 0
a = list(map(int, input().split()))
q = [1] * n
for i in range(n):
    if a[i] > k:
        break
    elif q[i] != 0:
        q[i] = 0
        p += 1
for i in range(1, n + 1):
    if a[-i] > k:
        break
    elif q[-i] != 0:
        q[-i] = 0
        p += 1
print(p)
