n = int(input())
b = [int(i) for i in input().split()]

A = [b[0]] + [min(b[i],b[i-1]) for i in range(1,n-1)] + [b[-1]]

print(sum(A))
