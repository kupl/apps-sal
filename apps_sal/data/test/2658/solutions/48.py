from collections import defaultdict
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
visited = [0] * N
current = 0
i = 1
while i <= K:
    current = A[current] - 1
    if visited[current] == 0:
        visited[current] = i
    else:
        loop = i - visited[current]
        num_loop = (K - i) // loop
        i += loop * num_loop
    i += 1
ans = current + 1
print(ans)
