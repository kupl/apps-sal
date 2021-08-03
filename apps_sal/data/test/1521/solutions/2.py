p, n = map(int, input().split())
s = set()
for i in range(n):
    x = int(input())
    if x % p in s:
        print(i + 1)
        return
    else:
        s.add(x % p)
print(-1)
