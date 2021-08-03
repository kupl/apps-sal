n = int(input())
a = list(map(int, input().split()))
c = 0
for i in a:
    if i == c + 1:
        c += 1
print(-1 if c == 0 else n - c)
