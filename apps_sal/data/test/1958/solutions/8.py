n, m = list(map(int, input().split()))
a = []
for i in range(n):
    s = input()
    if s == 'half':
        a.append(1)
    else:
        a.append(2)

def check(x):
    for i in range(n):
        if x == 0:
            return 0
        if a[i] == 1:
            x = x / 2
        else:
            x = x / 2 - 0.5
    if x < 0:
        return 0
    return 1

l = 0
r = 2**100
while l < r - 0.1:
    x = (l + r) / 2
    if check(x):
        r = x
    else:
        l = x
cnt = 0
for i in range(n):
    if a[i] == 2:
        cnt += 0.5
print(int(r * m - cnt * m))

