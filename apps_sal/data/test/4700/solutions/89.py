N, M = map(int, input().split())
H = list(map(int, input().split()))
OK = [True] * N
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())
    if H[A] < H[B]:
        OK[A] = False
    elif H[A] > H[B]:
        OK[B] = False
    else:
        OK[A] = False
        OK[B] = False

ans = sum(OK)
print(ans)
