n, m = map(int, input().split())
a = list(map(int, input().split()))
j = sum(a)/4/m
p = 0
for i in a:
    if i >= j:
        p += 1
if p >= m:
    print("Yes")
else:
    print("No")
