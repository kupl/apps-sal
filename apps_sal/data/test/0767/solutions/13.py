(n, z) = map(int, input().split())
lis = sorted(list(map(int, input().split())))
x = n // 2
res = 0
start = x
for i in range(x):
    if start < n:
        while lis[start] - lis[i] < z:
            if start < n - 1:
                start += 1
            else:
                break
        else:
            start += 1
            res += 1
    else:
        break
print(res)
