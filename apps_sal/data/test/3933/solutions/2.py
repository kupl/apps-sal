n = int(input())
a = list(map(int, input().split()))
s = a[1] - a[0]
f = 0
for i in range(len(a[:-1])):
    if a[i + 1] - a[i] != s:
        f = 1
if f == 1:
    print(a[-1])
else:
    print(a[-1] + a[-1] - a[-2])
