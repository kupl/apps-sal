n, t = list(map(int, input().split()))
k = 0
z = list(map(int, input().split()))
i = 0
while t > 86400 - z[i]:
    t -= 86400 - z[i]
    i += 1
print(i + 1)
