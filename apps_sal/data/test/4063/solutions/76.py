N = int(input())
d = list(map(int, input().split()))
d.sort()
i1 = N // 2
i2 = N // 2 - 1
result = d[i1] - d[i2]
print(result)
