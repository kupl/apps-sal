import copy
(h, w, k) = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        a = 0
        ci = copy.deepcopy(c)
        for s in range(h):
            if i >> s & 1 == 1:
                for tw in range(w):
                    ci[s][tw] = '.'
        for t in range(w):
            if j >> t & 1 == 1:
                for sh in range(h):
                    ci[sh][t] = '.'
        for ss in range(h):
            for tt in range(w):
                if ci[ss][tt] == '#':
                    a += 1
        if a == k:
            ans += 1
print(ans)
