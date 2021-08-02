x = int(input())
ans = 1
cnt = 1
for i in range(1, x):
    cnt = i
    for j in range(9):
        cnt *= i
        if cnt > x:
            break
        if cnt > ans:
            ans = cnt
print(ans)
