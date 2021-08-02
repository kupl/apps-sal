n = int(input())
L = [tuple(map(int, input().split(' '))) for i in range(n)]
ans = []
try:
    for l, r in reversed(L):
        d, a = 1, "("
        while d < l:
            d += len(ans[-1])
            a += ans.pop()
        if d > r: raise IndexError
        a += ")"
        ans.append(a)
except IndexError:
    print("IMPOSSIBLE")
    return
print("".join(reversed(ans)))
