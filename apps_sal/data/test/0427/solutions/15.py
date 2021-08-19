s = input()
arrIn = s.split()
n = int(arrIn[0])
m = int(arrIn[1])
x = int(arrIn[2])
y = int(arrIn[3])
l = 1
r = 2000000000.0
while l < r:
    mid = int((r + l) / 2)
    if n <= mid - int(mid / x) and m <= mid - int(mid / y) and (m + n <= mid - int(mid / (x * y))):
        r = mid
    else:
        l = mid + 1
else:
    print(r)
