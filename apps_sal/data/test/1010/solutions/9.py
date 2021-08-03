n = int(input())
l = list(map(int, input().split()))
ans = 1
p = -1
for i in range(len(l)):
    if l[i] == 1:
        if p == -1:
            p = i
            continue
        if i - p:
            ans *= i - p
        p = i
if p != -1:
    print(ans)
else:
    print(0)
