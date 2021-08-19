(N, M) = map(int, input().split())
A = list((input() for _ in range(N)))
B = list((input() for _ in range(M)))
ans = 'No'
for i in range(N - M + 1):
    for j in range(N - M + 1):
        if list((k[j:j + M] for k in A[i:i + M])) == B:
            ans = 'Yes'
print(ans)
