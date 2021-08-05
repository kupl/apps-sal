n = int(input())
l = list(map(int, input().split()))

ans = 0


def func(l, pn):
    ans = 0
    sum_ = 0
    for i in range(n):
        sum_ += l[i]
        if sum_ >= 0 and pn[i] < 0:
            ans += sum_ + 1
            sum_ = -1
        elif sum_ <= 0 and pn[i] > 0:
            ans += -sum_ + 1
            sum_ = 1
        else:
            continue
    return ans


pn1 = [1 if i % 2 == 0 else -1 for i in range(n)]
pn2 = [-1 if i % 2 == 0 else 1 for i in range(n)]

print(min(func(l, pn1), func(l, pn2)))
