n = int(input())
a = list(map(int, input().split()))
s = 0
pred = 0
for i in range(n):
    if a[i] == 1:
        s += 1
    elif pred == 1:
        s += 1
    pred = a[i]
if a[-1] == 0:
    s -= 1
if s < 0:
    s = 0
print(s)
