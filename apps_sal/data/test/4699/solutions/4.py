(n, k) = list(map(int, input().split()))
d = list(input().split())
ans = n
find = False
while find == False:
    p = str(ans)
    find = True
    for i in range(len(p)):
        if p[i] in d:
            find = False
            break
    if find == False:
        ans += 1
print(ans)
