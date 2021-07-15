n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(1, n):
    if a[i]*a[i-1] == 2:
        res += 3
        if i >= 2 and a[i-2] == 3:
            res -= 1
    elif a[i]*a[i-1] == 3:
        res += 4
    else:
        print('Infinite')
        return

print('Finite')
print(res)
