n = int(input())
a = list(map(int, input().split()))

s = set()

mx = 0
cnt = 0

for i in a:
    k = int(i)
    while k in s:
        s.remove(int(k))
        cnt = cnt - 1
        k = k + 1
    s.add(k)
    if mx < k:
        mx = k
    cnt = cnt + 1

print(mx - cnt + 1)
