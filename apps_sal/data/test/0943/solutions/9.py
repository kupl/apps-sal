n = int(input())
lst = list(map(int, input().split()))
s = 0
cnt = 0
lst.sort()
for i in lst:
    if i % 2 == 0:
        s += i
    else:
        s += i
        cnt += 1

if cnt % 2 == 0:
    print(s)
else:
    for i in range(n):
        if lst[i] % 2 == 1:
            s -= lst[i]
            break
    print(s)
