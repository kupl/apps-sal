import bisect
t = int(input())
j = 0
r = 0
R = []
for i in range(10 ** 5):
    j = 2 * j + 1
    s = j * (j + 1) // 2
    r += s
    R.append(r)
    if r > 10 ** 18:
        break
for _ in range(t):
    x = int(input())
    i = bisect.bisect_right(R, x)
    print(i)
