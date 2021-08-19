import sys
input = sys.stdin.readline
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
l = 0
r = 3 * 10 ** 5
while r - l > 1:
    m = (r + l) // 2
    ind = N - 1
    cnt = 0
    for a in A:
        while ind >= 0 and A[ind] + a < m:
            ind -= 1
        cnt += ind + 1
    if cnt >= M:
        l = m
    else:
        r = m
B = [0]
for a in A:
    B.append(B[-1] + a)
ans = 0
border = l
ind = N - 1
cnt = 0
for a in A:
    while ind >= 0 and A[ind] + a < border:
        ind -= 1
    cnt += ind + 1
    ans += a * (ind + 1) + B[ind + 1]
ans -= (cnt - M) * border
print(ans)
