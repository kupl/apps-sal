n = int(input())
a = list(map(int, input().split()))
l = []

s = sum(a)
cnt = 0
for i in range(n - 1):
    cnt += a[i]
    rem = s - cnt
    l.append(abs(cnt - rem))

print(min(l))
