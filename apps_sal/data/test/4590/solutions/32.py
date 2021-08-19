(N, M, K) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
curr = 0
A_index = 0
B_index = 0
while curr + A[A_index] <= K:
    curr += A[A_index]
    A_index += 1
    if A_index == N:
        break
while curr + B[B_index] <= K:
    curr += B[B_index]
    B_index += 1
    if B_index == M:
        break
ans = A_index + B_index
while A_index:
    A_index -= 1
    curr -= A[A_index]
    if B_index == M:
        break
    while curr + B[B_index] <= K:
        curr += B[B_index]
        B_index += 1
        if B_index == M:
            break
    ans = max(ans, A_index + B_index)
print(ans)
