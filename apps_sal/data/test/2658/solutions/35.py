N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

visited = [0 for _ in range(N)]
first_visit = [0 for _ in range(N)]

now = 0
flag = True
for i in range(10 ** 5 * 5):
    if first_visit[now] == 0:
        first_visit[now] = i

    visited[A[now] - 1] += 1
    now = A[now] - 1

    if i == K - 1:
        print((now + 1))
        flag = False
        break

if flag:
    num = 0
    for i in range(N):
        if visited[i] > 2:
            num += 1

    for i in range(N):
        if visited[i] >= 2:
            if K % num == first_visit[i] % num:
                print((i + 1))
                break

