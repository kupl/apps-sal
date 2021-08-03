n, w = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
a = arr[0]
b = arr[n]
if a * 2 > b:
    a = b / 2
else:
    b = 2 * a
print(min(w, a * n + b * n))
