from collections import Counter
n, k = map(int, input().split())
L = Counter(list(map(int, input().split())))
num = max(len(L) - k, 0)
ans = 0
if num == 0:
    print(0)
    return
L2 = sorted(L.values())
print(sum(L2[:num]))
