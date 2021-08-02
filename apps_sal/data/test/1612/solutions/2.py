n = int(input())

L = []
for i in range(n):
    m = list(map(int, input().split()))
    m = m[1:]
    L.append(sorted(m))

Ans = ["YES"] * n

for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        ind = -1
        for x in range(len(L[j])):
            if(L[j][x] == L[i][0]):
                ind = x
                break
        if(ind == -1):
            continue
        e = 0
        for x in range(ind, len(L[j])):
            if(L[j][x] == L[i][e]):
                e += 1
            if(e == len(L[i])):
                break
        if(e == len(L[i])):
            Ans[j] = "NO"
for i in range(n):
    print(Ans[i])
