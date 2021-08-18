n, k = map(int, input().split())
s = input()
if len(s) == 1:
    if k >= 1:
        print('0')
    else:
        print(s[0])
    return
cc = 0
arr = []
for i in s:
    arr.append(i)
if k == 0:
    print(s)
    return
if int(arr[0]) > 1:
    arr[0] = '1'
    cc += 1
for i in range(1, len(s)):
    if cc == k:
        break
    if int(arr[i]) != 0:
        arr[i] = '0'
        cc += 1
    if cc == k:
        break
print(''.join(arr))
