n = int(input())
arr = list(map(int, input().split()))
al = list((ai - (i + 1) for (i, ai) in enumerate(arr)))
al_s = sorted(al)


def func(ARR, x):
    tmp = 0
    for ai in ARR:
        tmp += abs(ai - x)
    return tmp


if n % 2 != 0:
    b = al_s[n // 2]
    ans = func(al, b)
else:
    b1 = al_s[n // 2]
    b2 = al_s[n // 2 - 1]
    ans = min(func(al, b1), func(al, b2))
print(ans)
