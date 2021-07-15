n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
am = a[0]
bm = min(b)
i = b[0] - 1
while i >= 2*am and a[-1] <= i and i > 0:
    i -= 1
i+=1
if i == 0 or not(i >= 2*am and a[-1] <= i and i > 0) or bm <= i:
    print(-1)
else:
    print(i)
