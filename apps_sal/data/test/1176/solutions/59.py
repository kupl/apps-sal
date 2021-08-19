n = int(input())
A = list(map(int, input().split()))
s = 0
m = 10 ** 9
nimus = 0
for a in A:
    s += abs(a)
    m = min(m, abs(a))
    if a < 0:
        nimus += 1
if nimus % 2 == 0:
    print(s)
else:
    print(s - 2 * m)
