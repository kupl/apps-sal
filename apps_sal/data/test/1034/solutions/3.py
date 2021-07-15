import heapq

X, Y, Z, K = list(map(int, input().split()))
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

checked = {(0, 0, 0)}
h = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]


def push(i, j, k):
    if i < X and j < Y and k < Z and (i, j, k) not in checked:
        heapq.heappush(h, (-(A[i] + B[j] + C[k]), i, j, k))
        checked.add((i, j, k))


for _ in range(K):
    s, i, j, k = heapq.heappop(h)
    print((-s))
    push(i + 1, j, k)
    push(i, j + 1, k)
    push(i, j, k + 1)

