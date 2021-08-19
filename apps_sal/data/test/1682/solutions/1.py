(n, k) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
que = [0] * n
for j in range(n):
    que[j] = [A[j] - B[j], j]
que.sort()
ans = 0
for j in range(n):
    if que[j][0] <= 0:
        k -= 1
        ans += A[que[j][1]]
    elif k > 0:
        k -= 1
        ans += A[que[j][1]]
    else:
        j -= 1
        break
for i in range(j + 1, n):
    ans += B[que[i][1]]
print(ans)
