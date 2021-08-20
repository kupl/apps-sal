n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if a[i] + a[i - 1] == 5:
        ans = -1
        break
    elif a[i] + a[i - 1] == 3:
        ans += 3
        if i >= 2 and a[i] == 2 and (a[i - 2] == 3):
            ans -= 1
    else:
        ans += 4
if ans == -1:
    print('Infinite')
else:
    print('Finite')
    print(ans)
