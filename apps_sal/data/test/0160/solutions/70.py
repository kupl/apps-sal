def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

N, K = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)
L = make_divisors(S)
ans = 0
for i in L:
    D = []
    for a in A:
        if a % i != 0:
            D.append(a % i)
    D.sort()
    L1 = [0]
    L2 = [0]
    for j in range(len(D)):
        L1.append(L1[-1] + D[j])
        L2.append(L2[-1] + i - D[len(D)-1-j])
    L2.reverse()
    
    for j in range(len(D)+1):
        if K >= max(L1[j], L2[j]):
            ans = max(ans, i)

print(ans)
