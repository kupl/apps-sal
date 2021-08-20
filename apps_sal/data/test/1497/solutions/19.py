n = int(input())
a = [list(input()) for i in range(n)]
Max = 0
for i in a:
    cnt = 0
    for j in a:
        if i == j:
            cnt += 1
    Max = max(cnt, Max)
print(Max)
