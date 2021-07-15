3

def _reverse(arr, left, right):
    n = len(arr)
    return arr[:left] + arr[-n+right:-n+left-1:-1] + arr[right+1:]

def check(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

t = int(input())
arr = [[-1*10**10, 0], [-1*10**10+1, 1]]
val = []
_number = 2
for i in input().split():
    val.append(int(i))
    arr.append([int(i), _number])
    _number += 1

arr.append([10**10, t+2])
arr.append([10**10+1, t+3])
t += 4

if check(val):
    print("yes\n1 1")
    return

arr.sort()

left = 1
for i in range(1, t):
    if arr[i-1][1]+1 == arr[i][1]:
        left = i
    else:
        break
right = t-2
for i in range(t-2, 0, -1):
    if arr[i+1][1]-1 == arr[i][1]:
        right = i
    else:
        break

left, right = arr[right-1][1]-2, arr[left+1][1]-2

flag = False
if left <= right:
    val = _reverse(val, left, right)
    flag = check(val)

if not flag:
    print('no')
else:
    print("yes\n%d %d" % (left+1, right+1))
