def gns():
    return [int(x) for x in input().split()]


(n, x) = gns()
if n == 1:
    if x == 1:
        print(0)
        quit()
    print(1)
    print(1)
    quit()
b = len(bin(x)) - 2
if x != 1:
    ans = [1]
else:
    ans = [2]
cur = 1
for i in range(n - 2):
    if cur == b - 1:
        cur += 1
    ans = ans + [1 << cur] + ans
    cur += 1
if x >= 1 << n:
    ans = ans + [1 << cur] + ans
y = x
print(len(ans))
print(' '.join(map(str, ans)))
