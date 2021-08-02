n = int(input())
s = input()
kol = [-1] * n
cur = 1
ind = 0
while ind < n:
    if kol[ind] != -1:
        ind += 1
    else:
        kol[ind] = cur
        best = s[ind]
        for i in range(ind + 1, n):
            if kol[i] != -1:
                continue
            else:
                if s[i] >= best:
                    kol[i] = cur
                    best = s[i]
        ind += 1
        cur += 1
print(max(kol))
for i in range(n):
    print(kol[i], end=" ")
