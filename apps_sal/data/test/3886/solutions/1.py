f0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
s0 = len(f0)
f10 = 'What are you doing while sending "'
s10 = len(f10)
f11 = '"? Are you busy? Will you send "'
s11 = len(f11)
f12 = '"?'
s12 = len(f12)
maxn = 100005
sz = [0] * maxn
sz[0] = s0
for i in range(1, maxn):
    if i < 500:
        sz[i] = s10 + s11 + s12 + 2 * sz[i - 1]
    else:
        sz[i] = 1e+100


def solve(n, k):
    while True:
        if k >= sz[n]:
            return '.'
        if n == 0:
            return f0[k]
        if k < s10:
            return f10[k]
        k -= s10
        if k < sz[n - 1]:
            n = n - 1
            continue
        k -= sz[n - 1]
        if k < s11:
            return f11[k]
        k -= s11
        if k < sz[n - 1]:
            n = n - 1
            continue
        k -= sz[n - 1]
        if k < s12:
            return f12[k]
        assert False


q = int(input())
ans = ''
for qid in range(q):
    (n, k) = list(map(int, input().split()))
    k -= 1
    ans += solve(n, k)
print(ans)
