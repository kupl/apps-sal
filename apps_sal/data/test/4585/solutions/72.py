import sys
X=int(input())

if not ( 1 <= X <= 10**9 ): return
res=0
count=0
for I in range(1,X+1):
    count += 1
    res += count
    if res >= X:
        print(count)
        return
