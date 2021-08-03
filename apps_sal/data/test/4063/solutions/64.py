n = int(input())
d = sorted(list(map(int, input().split())))
ans = d[n // 2] - d[n // 2 - 1]
print(ans)
