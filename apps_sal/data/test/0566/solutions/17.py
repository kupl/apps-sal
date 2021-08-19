3
c = list(map(int, input().split()))
c.sort()
print(min(sum(c) // 3, c[0] + c[1]))
