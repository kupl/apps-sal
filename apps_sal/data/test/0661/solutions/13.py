m, k = list(map(int, input().split()))

if m == 0:
    if k == 0:
        ans = [0, 0]
    else:
        ans = []

elif m == 1:
    if k == 0:
        ans = [0, 0, 1, 1]
    else:
        ans = []

elif k < 2 ** m:
    li = list(range(2 ** m))
    li.remove(k)
    ans = li + [k] + li[::-1] + [k]

else:
    ans = []

if ans:
    print((*ans))
else:
    print((-1))

