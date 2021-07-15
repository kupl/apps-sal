def run_length_compress(S):
    res = [[S[0], 1]]
    for c in S[1:]:
        if c == res[-1][0]:
            res[-1][1] += 1
        else:
            res.append([c, 1])
    return res


N, K = list(map(int, input().split()))
S = input()
cs = run_length_compress(S)
M = len(cs)

ans = 0
tot = 0
right = 0
zeros = 0
for left in range(M):
    while right < M and zeros + (cs[right][0] == "0") <= K:
        if cs[right][0] == "0":
            zeros += 1
        tot += cs[right][1]
        right += 1

    ans = max(ans, tot)

    if left == right:
        right += 1
    else:
        if cs[left][0] == "0":
            zeros -= 1
        tot -= cs[left][1]
print(ans)


