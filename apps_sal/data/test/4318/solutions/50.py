N = int(input())
hotel = list(map(int, input().split()))
i = 0
j = 0
cnt = 0
for i in range(N):
    q = 1
    for j in range(i):
        q = 0
        if hotel[j] > hotel[i]: break
        else:
            q = 1
    if q == 1:
        cnt += 1
print(cnt)
