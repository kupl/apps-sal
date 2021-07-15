from collections import Counter
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
ans = sum(A)
num = Counter(A)
for i in range(Q):
    b,c = map(int,input().split())

    ans += (c-b)*num[b]
    num[c] += num[b] 
    num[b] = 0
    
    print(ans)
