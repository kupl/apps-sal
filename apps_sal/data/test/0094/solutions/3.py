n = int(input())
k = list(map(int, list(input())))
m = len(k)
rec = [0] * (m + 1)
for i in range(m):
    u = rec[i] * n
    if k[i] > 0:
        d = 0
        for j in range(i, m):
            d = d * 10 + k[j]
            if d >= n:
                break
            if rec[j + 1]:
                rec[j + 1] = min(rec[j + 1], u + d)
            else:
                rec[j + 1] = u + d
            #print(d, j+1, rec)
    else:
        if rec[i + 1]:
            rec[i + 1] = min(rec[i + 1], u)
        else:
            rec[i + 1] = u
        #print(i, rec)
print(rec[-1])
