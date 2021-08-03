n, k = list(map(int, input().split()))

L = list(map(int, input().split()))

A = []
for i in range(0, n, k):
    A.append(list(L[i:i + k]))
z = n // k
ans = 0
for i in range(k):
    one = 0
    two = 0
    for j in range(z):
        if(A[j][i] == 1):
            one += 1
        else:
            two += 1
    ans += min(one, two)
print(ans)
