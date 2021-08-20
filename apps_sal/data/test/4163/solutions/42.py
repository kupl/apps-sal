n = int(input())
k = 0
flag = False
while n:
    (a, b) = map(int, input().split())
    if a == b:
        k += 1
    else:
        k = 0
    if k == 3:
        flag = True
        break
    n -= 1
print('Yes' if flag else 'No')
