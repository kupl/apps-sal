def check(a, b):
    if a[1] == b[1] and 1 <= abs(int(b[0]) - int(a[0])) <= 2:
        return True


arr = input().split()
d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1
mineq = 3 - max(d.values())
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])
if check(arr[0], arr[1]) or check(arr[1], arr[2]):
    mineq = min(mineq, 1)
if arr[0][1] == arr[1][1] == arr[2][1] and int(arr[2][0]) - int(arr[1][0]) == 1 and int(arr[1][0]) - int(arr[0][0]) == 1:
    mineq = 0
print(mineq)
