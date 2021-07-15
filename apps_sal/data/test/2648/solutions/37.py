import collections
N = int(input())
lsA = list(map(int,input().split()))
counterA = collections.Counter(lsA)
lsn = list(counterA.values())
rep = 0
even = 0
for i in lsn:
    if i % 2 ==1:
        rep += i//2
    else:
        rep += (i-1)//2
        even += 1
rep += -(-even//2)
ans = N-rep*2
print(ans)
