n = int(input())
arr = list(input())
ans = False
for i in range(n):
    if arr[i] == '*':
        for j in range(1, n // 4 + 1):
            x = 0
            for z in range(i, n, j):
                if arr[z] == '*':
                    x += 1
                else:
                    break
            if x >= 5:
                ans = True
if ans:
    print('yes')
else:
    print('no')
