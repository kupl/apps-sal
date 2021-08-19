N = int(input())
A = list(map(int, input().split()))
num = [0 for _ in range(N)]
for a in A:
    num[a - 1] += 1
num.sort()
cum = [0 for _ in range(N)]
cum[0] = num[0]
for i in range(1, N):
    cum[i] = cum[i - 1] + num[i]
index = N - 1
ans = N
for k in range(1, N + 1):
    while ans > 0:
        tmp_index = index
        while tmp_index >= 0 and num[tmp_index] > ans:
            tmp_index -= 1
        decided = N - tmp_index - 1
        rest_total = 0 if tmp_index < 0 else cum[tmp_index]
        if rest_total >= ans * (k - decided):
            index = tmp_index
            break
        ans -= 1
    print(ans)
