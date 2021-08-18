
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(4):
    ans = [-1] * n
    ans[0] = i
    flag = False
    for j in range(1, n):
        flag = False
        for k in range(4):
            if a[j - 1] == (k | ans[j - 1]) and b[j - 1] == (k & ans[j - 1]):
                ans[j] = k
                flag = True
        if not flag:
            break
    if flag:
        print("YES")
        print(*ans)
        return
print("NO")
