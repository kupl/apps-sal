n = int(input())
s_l = [ str(input()) for _ in range(n)  ]

m = int(input())
t_l = [ str(input()) for _ in range(m)  ]
d = {}
for s in s_l:
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
for t in t_l:
    if t not in d:
        d[t] = -1
    else:
        d[t] -= 1
ans = 0
for k, v in d.items():
    ans = max(v, ans)
print(ans)
