n, k = map(int, input().split())

t = 0
k = 240 - k

for j in range(n + 1):
    t += 5 * j
    if t > k:
        print(j - 1)
        break
else:
    print(j)
