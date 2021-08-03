A, B, X = map(int, input().split())
ans = 0


def cost(A, B, N):
    return A * N + B * len(str(N))


head = 0
tail = 10**9 + 1


while head <= tail:
    center = (head + tail) // 2

    if tail - head <= 10:
        tem = head
        break
    elif cost(A, B, center) < X:
        head = center + 1
    elif cost(A, B, center) > X:
        tail = center - 1

for N in range(max(0, tem - 10), min(tem + 10, 10**9 + 1)):
    if cost(A, B, N) <= X:
        ans = N

print(ans)
