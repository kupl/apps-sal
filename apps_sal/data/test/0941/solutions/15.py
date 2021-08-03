b, k = list(map(int, input().split()))
lst = list(map(int, input().split()))
if b % 2 == 0:
    if lst[-1] % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    cnt = 0
    for i in range(k):
        if lst[i] % 2 == 1:
            cnt += 1
    if cnt % 2 == 0:
        print("even")
    else:
        print("odd")
