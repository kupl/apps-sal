a = int(input())
for i in range(a):
    b = int(input())
    c = sorted(list(map(int, input().split())))[::-1]
    ans = 0
    co = 0
    for j in c:
        if j < co + 1:
            break
        co += 1
        ans += 1
        if co >= ans:
            ans = co
    print(ans)
    

