N, M, *cnt = open(0).read().split()
from collections import Counter
cnt = Counter(cnt)
for i in range(1,int(N)+1):
    print(cnt[str(i)])
