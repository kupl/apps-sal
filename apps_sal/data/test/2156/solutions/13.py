n = int(input())
s = list(map(int, input().split()))
acc = [0]
cur = 0
for a in s:
    cur += a
    acc.append(cur)
nq = int(input())
for i in range(nq):
    (l, r) = list(map(int, input().split()))
    print((acc[r] - acc[l - 1]) // 10)
