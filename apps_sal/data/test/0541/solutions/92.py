import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
want_list = [0] * (N + 1)
for _ in range(M):
    a, b = list(map(int, input().split()))
    want_list[b] = max(want_list[b], a)


cnt = 0
cutNo = 0
for idx, val in enumerate(want_list):
    if val > cutNo:
        cutNo = idx - 1
        cnt += 1
print(cnt)
