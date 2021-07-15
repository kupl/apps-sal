N = int(input())
table = [[int(i) for i in input().split()] for _ in range(N)]

cnt = 0

for i in range(N):
    if table[i][0] == table[i][1]:
        cnt += 1
        if cnt == 3:
            print("Yes")
            return
    else:
        cnt = 0

print("No")

