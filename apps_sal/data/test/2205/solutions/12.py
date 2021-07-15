n = int(input())
p = [int(i) for i in input().split()]
cap_P = 0
for i in p:
    cap_P ^= i
X = [0]*(n + 1)
for i in range(1, n + 1):
    X[i] = X[i-1]^i
for i in range(2, n + 1):
    a = n//i
    r = n%i
    cap_P ^= X[r]^(X[i-1] if a%2 else 0)
print(cap_P)

