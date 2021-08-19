n = int(input())
arr = list(input())
flag = False
for i in range(n):
    if arr[i] == '*':
        for d in range(1, n):
            begin = i
            for k in range(4):
                if begin + d < n and arr[begin + d] == '*':
                    begin += d
                else:
                    break
            else:
                flag = True
                break
    if flag:
        break
if flag:
    print('yes')
else:
    print('no')
