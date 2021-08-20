from collections import Counter
_ = input()
a = [int(i) for i in input().split()]
ans = 0
for (k, v) in Counter(a).items():
    if k < v:
        ans += v - k
    elif v < k:
        ans += v
else:
    print(ans)
