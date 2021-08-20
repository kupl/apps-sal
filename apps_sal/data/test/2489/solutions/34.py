from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
k = sorted(list(c.keys()))
kl = k[-1]
b = [1] * kl
cnt = 0
for i in k:
    if c[i] == 1 and b[i - 1] == 1:
        cnt += 1
    for j in range(1, kl + 1):
        if i * j > kl:
            break
        else:
            b[i * j - 1] = 0
print(cnt)
