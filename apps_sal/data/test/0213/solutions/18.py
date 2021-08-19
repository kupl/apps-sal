n, m = map(int, input().split())
min_ = 10000
max_ = 0
for i in range(m):
    k, f = map(int, input().split())
    if f > 1:
        min_ = min(k / (f - 1), min_)
    max_ = max(k / f, max_)
min_, max_ = max_, min_


if(min_ != int(min_)):
    min_ += 1
min_ = int(min_)

if (max_ != int(max_)):
    max_ += 1
max_ = int(max_)

#print(min_, max_)

s = set()
for i in range(max(1, min_), max_):
    b = n // i
    if (n % i) != 0:
        b += 1
    s.add(b)
if len(s) == 1:
    print(b)
else:
    print(-1)
