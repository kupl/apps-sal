import itertools
n, k = map(int, input().split())
d = list(input().split())
num = [str(i) for i in range(10)]
for i in range(k):
    num.remove(d[i])

ans = []
for i in itertools.product(num, repeat=len(str(n))):
    s = int(''.join(i))
    if s >= n:
        ans.append(s)

if len(ans) == 0:
    for i in itertools.product(num, repeat=len(str(n)) + 1):
        s = int(''.join(i))
        if s >= n:
            ans.append(s)
    print(min(ans))

else:
    print(min(ans))
