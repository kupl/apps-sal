N, K = map(int, input().split())
*D, = input().split()
ok = 1
while ok:
    ans = list(str(N))
    ok = 0
    for a in ans:
        if a in D:
            ok = 1
    N += 1
print(''.join(ans))
