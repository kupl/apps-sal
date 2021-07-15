n = int(input())
A = [int(x) for x in input().split()]
A = A+A
s,f = list(map(int,input().split()))

l = f-s
S = sum(A[:l])
mi = 0
mS = S
ans = (s-1-mi)%n + 1
for i in range(n-1):
    S = S + A[i+l] - A[i] 
    if mS == S:
        mi = i+1
        ans = min(ans, (s-1-mi)%n + 1) # Update min
    if mS < S:
        mS = S
        mi = i+1
        ans = (s-1-mi)%n + 1 # Set min
print(ans)

