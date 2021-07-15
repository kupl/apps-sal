n, k = map(int, input().split())
s = input()

if k == 0:
    print(s)
    return
if n == 1:
    print(0)
    return

first = True
ans = []
cnt = 0
for i in s:
    if first and i != '1' and cnt < k:
        print(1, end='')
        cnt += 1
    elif not first and i != '0' and cnt < k:
        print(0, end='')
        cnt += 1
    else:
        print(i, end='')
    
    first = False

