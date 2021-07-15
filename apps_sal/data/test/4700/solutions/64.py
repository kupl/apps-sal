N, M = map(int, input().split())
H = list(map(int, input().split()))
array = [0] * N
ans = 0

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    array[A] = max(array[A], H[B])
    array[B] = max(array[B], H[A])

for j in range(N):
    if array[j] < H[j]:
      ans += 1

print(ans)
