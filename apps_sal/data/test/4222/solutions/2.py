N, K = map(int, input().split())
sunukes = [0 for k in range(N)]
for k in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        sunukes[a - 1] += 1
    assert len(A) == d
print(len([k for k in sunukes if k == 0]))
