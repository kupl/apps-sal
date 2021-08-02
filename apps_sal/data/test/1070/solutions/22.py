n, k = list(map(int, input().split()))
Max = 0
m = 1
H = list(map(int, input().split()))
for i in range(n - 1):
    if H[i] != H[i + 1]:
        m += 1
    else:
        if m > Max:
            Max = m
        m = 1
if m > Max:
    Max = m
print(Max)
