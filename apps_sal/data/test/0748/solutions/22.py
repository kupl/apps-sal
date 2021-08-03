n = int(input())
a = list(map(int, input().split()))
t = [0] * 8
for x in a:
    t[x] += 1
if t[5] > 0 or t[7] > 0 or t[1] * 3 < n:
    print(-1)
else:
    a = t[4]
    c = t[3]
    b = t[2] - a
    if b < 0 or (a + b + c) != t[1] or (b + c) != t[6]:
        print(-1)
        return
    for i in range(a):
        print('1 2 4')
    for i in range(b):
        print('1 2 6')
    for i in range(c):
        print('1 3 6')
