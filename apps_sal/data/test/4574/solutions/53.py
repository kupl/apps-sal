n = int(input())
A = list(map(int, input().split()))
A.sort()
l = 0
h = 0
i = n-1
while i >= 0:
    if i > 0 and A[i] == A[i-1] and l == 0:
        l = A[i]
        i -= 2
    elif i > 0 and A[i] == A[i-1] and h == 0:
        h = A[i]
        break
    else:
        i-=1
print (l*h)
