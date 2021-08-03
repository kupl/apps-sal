n = int(input())
l = [tuple(map(int, input().split())) for i in range(n)]

cnt = 0
for i in l:
    cnt += (i[1] - i[0] + 1)
print(cnt)
