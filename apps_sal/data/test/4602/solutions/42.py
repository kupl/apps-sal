N = int(input())
K = int(input())
X = [int(n) for n in input().split()]

ans = 0

for x in X:
    diff = abs(K - x)
    if diff < x:
        ans += diff
    else:
        ans += x
print((2*ans))

