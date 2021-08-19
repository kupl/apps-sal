def check(arr):
    for i in range(len(arr)):
        if arr[i] == ['x', 'x', 'x']:
            return True
    for i in range(3):
        if arr[0][i] == 'x' and arr[1][i] == 'x' and (arr[2][i] == 'x'):
            return True
    if arr[0][0] == 'x' and arr[1][1] == 'x' and (arr[2][2] == 'x'):
        return True
    elif arr[0][2] == 'x' and arr[1][1] == 'x' and (arr[2][0] == 'x'):
        return True
    return False


arr = []
for _ in range(3):
    arr.append(list(map(int, input().split(' '))))
n = int(input())
for _ in range(n):
    b = int(input())
    for i in range(len(arr)):
        tmp_arr = []
        for ele in arr[i]:
            if b == ele:
                tmp_arr.append('x')
            else:
                tmp_arr.append(ele)
        arr[i] = tmp_arr
if check(arr) == True:
    print('Yes')
else:
    print('No')
