from collections import Counter
n, k = map(int, input().split())
Xl = list(map(int, input().split()))
Xdic = Counter(Xl)
valuelist = sorted(list(Xdic.values()), reverse=True)
print(sum(valuelist[k:]))
