n, m = map(int, input().split())
p_s = [ list(map(str, input().split())) for _ in range(m) ]
ac = [False] * n
wa = [0] * n
for p, s in p_s:
    if ac[int(p)-1] is False:
        if s == 'AC':
            ac[int(p)-1] = True
        else:
            wa[int(p)-1] += 1
print(sum([1 for i in ac if i == True ]), sum([i for i,j in zip(wa,ac) if j == True ]))
