N = int(input())
l = [list(map(int, input().split())) for i in range(N)]
l.sort(key=lambda x: x[2], reverse=True)

for i in range(101):
    for j in range(101):
        h = l[0][2] + abs(i - l[0][0]) + abs(j - l[0][1])
        for k in range(N):
            tmp = max(h - abs(i - l[k][0]) - abs(j - l[k][1]), 0)
            if tmp != l[k][2]:
                break
            elif k == N-1:
                X = i
                Y = j
                H = h
print(X,Y,H)
