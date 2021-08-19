(n, k) = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cnt = 0
for a in A:
    while a > 2 * k:
        cnt += 1
        k *= 2
    k = max(k, a)
print(cnt)
