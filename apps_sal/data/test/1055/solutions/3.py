n = m = int(input())
A = [int(x) for x in input().split()]

while True:
    if any(sorted(A[i:i+m]) == A[i:i+m] for i in range(0,n,m)):
        print(m)
        break
    m //= 2

