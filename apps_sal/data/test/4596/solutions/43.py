n = int(input())
a = list(map(int, input().split()))
t = True
ans = 0
while t:
    for i in range(n):
        if a[i] % 2 == 1:
            t = False
            break
        else:
            a[i] /= 2
    if t:
        ans += 1
print(ans)
