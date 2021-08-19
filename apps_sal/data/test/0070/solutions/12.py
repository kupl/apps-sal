a = list(input().split())
n = a[0]
k = int(a[1])
c = 0
f = 0
for x in range(-1, -len(n) - 1, -1):
    if n[x] == '0':
        c = c + 1
        if c == k:
            print(-x - k)
            f = 1
            break
if f == 0:
    print(len(n) - 1)
