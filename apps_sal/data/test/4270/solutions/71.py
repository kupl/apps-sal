def cumsum(n,A):
    s = [0]*(n+1)
    s[0] = A[0]
    for i in range(len(A)):
        s[i+1] = (s[i] + A[i])/2
    return s

n = int(input())
v = sorted(list(map(int,input().split())))

for i in range(n-1):
    s = cumsum(n,v)
print(s[-1])
