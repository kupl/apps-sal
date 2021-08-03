n = int(input())
a = sorted([int(x) for x in input().split()], reverse=True)
ans = sum([a[(i + 1) // 2] for i in range(n - 1)])
print(ans)
