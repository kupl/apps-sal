n, k = list(map(int, input().split()))
t = 4 * 60 - k
i = 1
while i <= n and t >= 5 * i:
    t -= 5 * i
    i += 1
i -= 1
print(i)


