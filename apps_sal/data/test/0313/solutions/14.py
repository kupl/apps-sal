n = int(input())
a = list(map(int, input().split()))

ans = 0
for i, e in enumerate(a):
    if e == 1:
        ans += 1
    else:
        if i < len(a) - 1 and i > 0 and\
         a[i + 1] == 1 and a[i - 1] == 1:
            ans += 1

print(ans)

