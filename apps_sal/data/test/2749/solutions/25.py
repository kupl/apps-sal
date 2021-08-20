(H, W) = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
ans = []
for (i, a) in enumerate(A):
    ans.extend([str(i + 1)] * a)
for i in range(H):
    l = ans[i * W:(i + 1) * W]
    if i % 2:
        l.reverse()
    print(' '.join(l))
