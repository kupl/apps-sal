n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in li:
    cnt += i[1] - i[0] + 1
print(cnt)
