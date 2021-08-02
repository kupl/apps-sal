def solve(n, aaa, bbb):
    ccc = [a1 ^ a2 for a1, a2 in zip(aaa, aaa[1:])] + [aaa[-1] ^ aaa[0]]
    ddd = [b1 ^ b2 for b1, b2 in zip(bbb, bbb[1:])] + [bbb[-1] ^ bbb[0]]

    ans = []

    m = 2147483647
    g = 1000000007
    s = 0
    for c in ccc:
        s = (s * g + c) % m
    t = 0
    for d in ddd:
        t = (t * g + d) % m
    u = pow(g, n, m) - 1
    for i in range(n):
        if s == t:
            ans.append((i, aaa[i] ^ bbb[0]))
        s = (s * g - ccc[i] * u) % m
    ans.sort()
    return ans


n = int(input())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))
ans = solve(n, aaa, bbb)
print((''.join('{} {}\n'.format(*answer) for answer in ans)))
