import itertools
N = int(input())
s = len(str(N))
ans = 0
b1 = list(itertools.product('0357', repeat=s))
for k in b1:
    t = int(''.join(k))
    if N < t:
        break
    x = set(str(t))
    y = x - {'3', '5', '7'}
    if len(y) == 0 and len(x - y) == 3:
        ans += 1
print(ans)
