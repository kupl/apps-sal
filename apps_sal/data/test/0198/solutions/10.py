n = int(input())
if n % 2: print(0)
else:
    k = n // 2
    cnt = k // 2
    if k % 2 == 0: cnt -= 1
    print(cnt)

