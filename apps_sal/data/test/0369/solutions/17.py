import bisect

N, M = list(map(int, input().split()))
S = input()

ok = True
cnt = 0
for c in S:
    if c == "1":
        cnt += 1
        if cnt == M:
            ok = False
            break
    else:
        cnt = 0

ngo_pos = [0 for _ in range(N + 1)]
most_neighbor_zero_pos = N
for i in range(N, -1, -1):
    if S[i] == "0":
        ngo_pos[i] = i
        most_neighbor_zero_pos = i
    else:
        ngo_pos[i] = most_neighbor_zero_pos

if not ok:
    print((-1))
else:
    ans = []
    pos = N
    while pos > 0:
        npos = ngo_pos[max(0, pos - M)]
        ans.append(pos - npos)
        pos = npos
    print((" ".join(map(str, ans[::-1]))))
