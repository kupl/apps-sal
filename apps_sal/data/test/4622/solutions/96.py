from collections import Counter
N=int(input())
Alist=list(map(int,input().split()))
count=Counter(Alist)
flag=True
for value in count.values():
    if value>1:
        flag=False
print('YES' if flag else 'NO')
