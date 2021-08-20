n = int(input())
arr = list(map(int, input().strip().split()))
k = min(arr)
h = max(arr)
s = 0
for i in arr:
    if i >= 0:
        s += i
    else:
        s -= i
if n == 1:
    print(arr[0])
elif k < 0 and h >= 0:
    print(s)
elif k >= 0:
    print(s - 2 * k)
else:
    print(s + 2 * h)
