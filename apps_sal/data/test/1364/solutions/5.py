n = int(input())
a = list(map(int, input().split()))
t = 0
u = 0
ans = 0
if a[0] == 1:
    t += 1
else:
    u += 1
for i in range(1, len(a)):
    if a[i] == 1:
        if a[i] == a[i - 1]:
            t += 1
        else:
            t = 1
    else:
        if a[i] == a[i - 1]:
            u += 1
        else:
            u = 1
    ans = max(ans, min(u, t))

print(ans * 2)
