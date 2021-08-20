from sys import stdin
n = int(stdin.readline().strip())
s = stdin.readline().strip()
arr = [0 for i in range(10)]
for i in range(n):
    if s[i] == 'L':
        for j in range(10):
            if arr[j] == 0:
                arr[j] = 1
                break
    elif s[i] == 'R':
        for j in range(9, -1, -1):
            if arr[j] == 0:
                arr[j] = 1
                break
    else:
        arr[int(s[i])] = 0
for i in arr:
    print(i, end='')
