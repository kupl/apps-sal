n = int(input().strip())
a = list(map(int, input().split()))

cnt = [0 for i in range(10**5)]
a = sorted(a)
s = sum(a)

for i in range(n):
    cnt[a[i] - 1] += 1

q = int(input().strip())

for i in range(q):
    b, c = list(map(int, input().split()))
    s += c * cnt[b - 1] - b * cnt[b - 1]
    cnt[c - 1] += cnt[b - 1]
    cnt[b - 1] = 0
    print(s)
