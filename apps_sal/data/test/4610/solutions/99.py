n,k= map(int,input().split())
Xl = list(map(int,input().split()))
from collections import Counter
Xdic = Counter(Xl)
valuelist = sorted(list(Xdic.values()), reverse=True)
print(sum(valuelist[k:]))
