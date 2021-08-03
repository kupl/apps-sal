import itertools
n = int(input())
a = list(map(int, input().split()))

n_acc = itertools.accumulate(a)
#r_acc = itertools.accumulate(a[::-1])
# 1, 3, 6, 10, 15 ,21
# 1 vs 20
# 3 vs
#print(n_acc, r_acc)


sigma = sum(a)
ans = 10 ** 16

for i, val in enumerate(n_acc):
    if (i == len(a) - 1):
        break

    rest = sigma - val
    ans = min(abs(val - rest), ans)


print(ans)
