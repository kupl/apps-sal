n = int(input())
csf = [list(map(int, input().split())) for i in range(n - 1)]
ans1 = []
for j in range(n - 1):
    requ_time = csf[j][1] + csf[j][0]
    for i in range(j, n - 1):
        if i != j:
            if requ_time <= csf[i][1]:
                requ_time += csf[i][0] + (csf[i][1] - requ_time)
            else:
                requ_time += csf[i][0] + (csf[i][2] - (requ_time - csf[i][1]) % csf[i][2]) % csf[i][2]
    ans1.append(requ_time)
for i in ans1:
    print(i)
print(0)
