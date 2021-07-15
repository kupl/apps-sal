n = int(input())
l = [*map(int, input().split())]
res = l[2]
res ^= min(l)
print(res + 2)
