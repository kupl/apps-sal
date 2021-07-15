def test(x):
    nonlocal arr, n
    s = 0
    for i in range(n):
        s += arr[i]
        if s > x:
            return False
        elif s == x:
            s = 0
    return s == 0



n = int(input())
oarr = list(map(int, list(input())))
arr = []
for el in oarr:
    if el:
        arr.append(el)
    else:
        n -= 1
s = 0
for i in range(n - 1):
    s += arr[i]
    if test(s):
        print("YES")
        break
else:
    if n == 0:
        print("YES")
    else:
        print("NO")

