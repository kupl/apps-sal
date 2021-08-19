N = int(input())
a = list((int(x) for x in input().split()))
ans = 0
flag = True
while flag:
    for i in range(N):
        if a[i] % 2 == 0:
            a[i] /= 2
        else:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
