N = int(input())
S = input()
ok, ng = 0, N + 1
while abs(ok - ng) > 1:
    x = (ok + ng) // 2
    check = set()
    for i in range(N - x + 1):
        check.add(S[i: i + x])
        if S[i + x: i + 2 * x] in check:
            ok = x
            break
    else:
        ng = x

print(ok)
