n = int(input())
d = sorted(list(map(int, input().split())))

x = d[n//2-1]
y = d[n//2]
print(y-x)
