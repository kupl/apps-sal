n, m, k = list(map(int, input().split()))
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = set(map(int, input().split()))
pup = list(zip(p, s, list(range(1, n + 1))))
pup.sort(reverse=True)
used = [False] * m
res = 0
for i in range(n):
    v, sc, num = pup[i]
    if used[sc - 1] and num in c:
        res += 1
    used[sc - 1] = True
print(res)
