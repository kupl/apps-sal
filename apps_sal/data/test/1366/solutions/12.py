n = int(input())
bottle = []
for i in range(n):
    bottle.append(list(map(int, input().split())))
count = 0
check = []
for i in range(n):
    check.append(False)
for i in range(n):
    for j in range(n):
        if i == j :
            continue
        else:
            if bottle[i][1] == bottle[j][0] and check[j] == False:
                count += 1
                check[j] = True
            
print(n-count)
