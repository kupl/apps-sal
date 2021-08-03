n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))
cd = []
for i in range(n):
    cd.append(list(map(int, input().split())))
cd.sort()
ab.sort(key=lambda x: x[1], reverse=True)
flag_ab = [False for i in range(n)]
count = 0
for i in range(n):
    c, d = cd[i][0], cd[i][1]
    for j in range(n):
        if flag_ab[j] == True:
            continue
        a, b = ab[j][0], ab[j][1]
        if c > a and d > b:
            flag_ab[j] = True
            count += 1
            break
print(count)
