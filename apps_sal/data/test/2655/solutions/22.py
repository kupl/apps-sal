n = int(input())
a = sorted(list(map(int, input().split())))
s = a[::]
ans = 0
c = 0
for i in range(n-1):
    if i == 0:
        ans += s.pop()
    else:
        if c == 0:
            ans += s[-1]
            c += 1
        elif c == 1:
            ans += s.pop()
            c = 0

print(ans)
