n = int(input())
a = list(map(int, input().split()))
ans = 0
flag = False
while flag == False:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] /= 2
        else:
            flag = True
            break
    else:
        ans += 1
print(ans)
