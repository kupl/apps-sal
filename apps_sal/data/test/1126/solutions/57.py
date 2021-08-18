N, X, M = list(map(int, input().split()))

pre_loop_sum = 0
all_loop_sum = 0
incomplete_loop_sum = 0

loop_flag = False

L = []
L.append(X % M)

S = set()

for i in range(1, N):
    X = pow(X, 2, M)

    if X in S:
        loop_flag = True
        break
    else:
        L.append(X)
        S.add(X)

index = L.index(X)

len_L = len(L)

if loop_flag:
    pre_loop_sum = sum(L[0:index])

    loop_sum = sum(L[index:len_L])
    loop_len = len_L - index
    loop_count = (N - index) // loop_len

    all_loop_sum = loop_count * loop_sum

    incomplete_loop_len = (N - index) % loop_len
    incomplete_loop_sum = sum(L[index:index + incomplete_loop_len])
else:
    pre_loop_sum = sum(L)

ans = pre_loop_sum + all_loop_sum + incomplete_loop_sum

print(ans)
