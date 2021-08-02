N = int(input())
W = []
for i in range(N):
    W.append(list(map(int, input().split())))

W = sorted(W, key=lambda x: (x[1], x[0]))
now = 0
for w in W:
    # print(now,w[0])
    if now + w[0] > w[1]:
        print("No")
        return
    now += w[0]
print("Yes")
