n = int(input())
a = input()

b = input()
diff = []
for i in range(n):
    if(a[i] != b[i]):
        posai = -1
        posbi = -1

        for j in range(len(diff)):
            if(a[i] in diff[j]):
                posai = j
            if(b[i] in diff[j]):
                posbi = j
        if(posbi != -1 and posai != -1):
            if(posbi == posai):
                pass
            else:
                diff[posai] = diff[posai].union(diff[posbi])
                del diff[posbi]
        elif(posbi != -1):
            diff[posbi].add(a[i])
        elif(posai != -1):
            diff[posai].add(b[i])
        else:
            diff.append({a[i], b[i]})
# print(diff)
diff2 = []
for i in diff:
    diff2.append([])
    for j in i:
        diff2[-1].append(j)
ans = 0
for i in diff2:
    ans += len(i) - 1
print(ans)
for i in diff2:
    for j in range(1, len(i)):
        print(i[j - 1], i[j])
