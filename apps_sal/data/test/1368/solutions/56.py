n, a, b = list(map(int, input().split()))
V = list(map(int, input().split()))

V.sort(reverse=True)
s = 0
m = V[a - 1]
ans = sum(V[:a]) / a
print(ans)
cnt = V.count(m)
left = V.index(m)
ans = 0
memo = {}


def combi(m, k):
    if m * 100 + k in memo:
        return memo[m * 100 + k]
    elif k == 0:
        return 1
    else:
        memo[m * 100 + k] = combi(m, k - 1) * (m - k + 1) // k
        return memo[m * 100 + k]


if left == 0:
    for i in range(a, min(b, cnt) + 1):
        ans += combi(cnt, i)
else:
    ans += combi(cnt, a - left)
    # if (sum(V[:a])/a).is_integer():
    #     ans *= pow(2,V.count(int(V[:a]/a)))
print(ans)
