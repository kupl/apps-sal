N, P = list(map(int, input().split()))
S = input()
now = 0
hyou = [0] * P
hyou[0] = 1
cnt = 1
ans = 0

if P == 2 or P == 5:
    for i, t in enumerate(S[::-1]):
        temp = int(t)
        if temp % P == 0:

            ans += N - i
    print(ans)
    return

for i, t in enumerate(S[::-1]):
    now = (now + int(t) * pow(10, i, P)) % P
    ans += hyou[now]
    hyou[now] += 1

print(ans)
