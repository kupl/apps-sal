from bisect import bisect_right

N, M = list(map(int, input().split()))
S = [N - i for i, s in enumerate(input()) if s == '0']
S = S[::-1]

ans = []
now = 0
while now < N:
    i = bisect_right(S, now + M) - 1

    if S[i] == now:
        print('-1')
        return

    ans.append(S[i] - now)
    now = S[i]

print((*ans[::-1]))
