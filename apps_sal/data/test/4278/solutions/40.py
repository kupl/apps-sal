import collections
S=[]
n=int(input())
for _ in range(n):
    s=input()
    S.append(str(sorted(s)))
ss=collections.Counter(S)
count=0
for i in ss.values():
    count+=int(i*(i-1)/2)
print(count)
