n = int(input())
a = list(input())
b = list(input())
ans = 0
ansl = []
for i in range(len(b)):
    flag = True
    for j in range(i, len(a)):
        if a[j] == b[i]:
            for k in range(j - i):
                ans += 1
                a[j-k], a[j-k-1] = a[j-k-1], a[j-k]
                ansl.append(j - k)
            flag = False
            break
    if flag:
        print(-1)
        return
print(ans)
print(*ansl)
