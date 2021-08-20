(n, k) = list(map(int, input().split()))
t = 240 - k
s = 0
for i in range(1, n + 1):
    if t < 0:
        print(s - 1)
        break
    s += 1
    t -= 5 * i
else:
    if t < 0:
        print(s - 1)
    else:
        print(s)
