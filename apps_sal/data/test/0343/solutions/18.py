(n, k, p, x, y) = map(int, input().split())
A = list(map(int, input().split()))
cnt = n // 2 + 1
for i in A:
    if i >= y:
        cnt -= 1
cnt = max(cnt, 0)
if n - k < cnt:
    print(-1)
else:
    B = [y] * cnt + [1] * (n - k - cnt)
    if sum(A) + sum(B) > x:
        print(-1)
    else:
        for i in B:
            print(i, end=' ')
