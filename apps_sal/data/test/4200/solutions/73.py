(N, M) = map(int, input().split())
A = list(map(int, input().split()))
ok = [item for item in A if item >= sum(A) / (4 * M)]
if len(ok) >= M:
    print('Yes')
else:
    print('No')
