n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
x = 0
if k == 1:
    x = min(a)
elif k == 2:
    x = max(a[0], a[n - 1])
else:
    x = max(a)
print(x)

#print(" ".join(map(str,a)))
