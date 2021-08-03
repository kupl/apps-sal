s = input()
arr = []
for i in s:
    arr.append(i)
c = 'a'
d = 0
for i in range(len(arr)):
    if arr[i] <= c:
        arr[i] = c
        if c == 'z':
            d = 1
            break
        c = chr(ord(c) + 1)

if d == 0:
    print(-1)
else:
    print(*arr, sep='')
