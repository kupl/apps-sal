n = int(input())
A = list(map(int, input().split()))

def search(x):
    b = n
    r = 0
    y = 0
    D = [0]*(2*n+1)
    for i in range(n):
        D[b] += 1
        if A[i] < x:
            r += D[b]
            b += 1
        else:
            b -= 1
            r -= D[b]   
        y += r
    return y

S = sorted(A)
l = 0
r = n
m = n // 2
c = n * (n + 1) // 2

while True:
    if search(S[m]) <= c // 2:
        if m == n - 1:
            break
        elif search(S[m + 1]) > c // 2:
            break
        else:
            l = m
            m = (m + r) // 2
    else:
        r = m + 1
        m = (m + l) // 2
        
print((S[m]))

