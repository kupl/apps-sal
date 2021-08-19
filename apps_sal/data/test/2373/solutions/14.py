N = int(input())
p = list(map(int, input().split()))
temp = 1
ans = 0
for i in range(N):
    if p[i] == i + 1:
        temp += 1
    else:
        if temp == 1:
            pass
        else:
            ans += temp // 2
        temp = 1
ans += temp // 2
print(ans)
