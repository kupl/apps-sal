(N, M) = map(int, input().split())
A = list((input() for _ in range(N)))
B = list((input() for _ in range(M)))
ans = 'No'
for i in range(N - M + 1):
    for j in range(N - M + 1):
        if [k[j:j + M] for k in A[i:i + M]] == B:
            ans = 'Yes'
            '\n        for k in A[i:i + M]:\n            if k[j:j + M]  == B:\n                ans = "Yes"\n        '
print(ans)
