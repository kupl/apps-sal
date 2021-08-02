n = int(input())
a = list(map(int, input().split()))
c = 0
s = 0
ma = 10**6
for i in a:
    if i < 0:
        c += 1
        c %= 2
    s += abs(i)
    ma = min(ma, abs(i))
if c == 1:
    print((s - 2 * ma))
else:
    print(s)
