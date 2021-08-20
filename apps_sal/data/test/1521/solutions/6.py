(p, n) = map(int, input().split())
s = set()
ex = 0
for i in range(n):
    x = int(input())
    if x % p in s:
        print(i + 1)
        ex = 1
        break
    s.add(x % p)
if ex == 0:
    print(-1)
