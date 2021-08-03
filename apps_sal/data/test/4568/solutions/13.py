N = int(input())
S = input()

max_cnt = 0
for i in range(1, N):
    x = set(S[0:i])
    y = set(S[i:N])
    x_y = len(x & y)

    if x_y > max_cnt:
        max_cnt = x_y

print(max_cnt)
