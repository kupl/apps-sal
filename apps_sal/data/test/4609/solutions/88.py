n = int(input())
a = [int(input()) for _ in range(n)]
import collections
cnt = 0
b = collections.Counter(a)
for k in b:
    if b[k]%2==1:
        cnt +=1
print(cnt)
