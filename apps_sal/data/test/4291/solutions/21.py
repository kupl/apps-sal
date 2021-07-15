N,Q = map(int,input().split())
S = input()
c = []
count = 0
for i in range(N-1):
    if S[i] == "A" and S[i+1] == "C":
        count += 1
    c.append(count)
for i in range(Q):
    l,r = map(int,input().split())
    if l == 1:
        print(c[r-2]-0)
    else:
        print(c[r-2]-c[l-2])
