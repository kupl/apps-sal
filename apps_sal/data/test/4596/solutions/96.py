n = int(input())
a = [int(i) for i in input().split()]
ans = -1
true = 1
while true == 1:
    for i in range(n):
        if a[i] % 2 != 0:
            true = 0
            break
        else:
            a[i] /= 2
    ans += 1
print(ans)
