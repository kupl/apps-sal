n = int(input())
l = list(map(int, input().split(' ')))
l = sorted(l)
print(l[(n - 1) // 2])
