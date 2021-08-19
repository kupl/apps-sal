import itertools
(n, k) = list(map(int, input().split()))
x = (0,) + tuple(itertools.accumulate(list(map(int, input().split()))))
ansa = ansb = 0
for i in range(2 * k, n + 1):
    if ansa < x[i - k] - x[i - 2 * k]:
        anst = i - 2 * k + 1
        ansa = x[i - k] - x[i - 2 * k]
    if ansb < ansa + x[i] - x[i - k]:
        ans1 = anst
        ans2 = i - k + 1
        ansb = ansa + x[i] - x[i - k]
print(ans1, ans2)
