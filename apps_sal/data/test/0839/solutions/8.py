a = []
for i in range(5):
    a.append(list(map(int, input().split())))
    
used = [False] * 5
ans = 0
for i1 in range(5):
    used[i1] = True
    for i2 in range(5):
        if not used[i2]:
            used[i2] = True
            
            for i3 in range(5):
                if not used[i3]:
                    used[i3] = True
                    for i4 in range(5):
                        if not used[i4]:
                            used[i4] = True
                            for i5 in range(5):
                                if not used[i5]:
                                    m = 0
                                    used[i5] = True
                                    o = [i1, i2, i3, i4, i5]
                                    for j in range(5):
                                        for i in range(0, len(o) - 1, 2):
                                            m += a[o[i]][o[i + 1]] + a[o[i + 1]][o[i]]
                                        o = o[1:]
                                    if m > ans:
                                        ans = m
                                    used[i5] = False
                            used[i4] = False
                    used[i3] = False
            used[i2] = False
    used[i1] = False
print(ans)
