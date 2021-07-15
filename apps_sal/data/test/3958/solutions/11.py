s = input()
res, p = [], -1

for i in range(len(s)):
    j = i + 1
    if s[i] == '0':
        if p > -1:
            res[p].append(j)
            p -= 1
        else:
            res.append([j])
    else:
        p += 1
        if p >= len(res):
            print(-1)
            return
        res[p].append(j)  

if p != -1:
    print(-1)
    return    

print(len(res))
for x in res:
    print(len(x), *x)

