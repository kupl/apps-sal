n, k = list(map(int, input().split()))

L = list(map(int, input().split()))

L.sort(reverse=True)

S = {}


for i in range(n):

    if(L[i] * k in S):

        continue

    S[L[i]] = 1

print(len(S))
