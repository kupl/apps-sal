import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    S = input().rstrip()
    Query.append((N, S))

for N, S in Query:
    i1 = N
    while i1 > 0 and S[i1-1] == "1":
        i1 -= 1
    i2 = -1
    while i2 +1< N-1 and S[i2+1] == "0":
        i2 += 1
    
    if i2 + 1 == i1:
        tmp = ""
    else:
        tmp = "0"
    ans = "0"*(i2+1) + tmp + "1"*(N-i1)
    print(ans)
