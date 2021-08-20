N = int(input())
restaurant = [[input().split(), i + 1] for i in range(N)]
resta_new = sorted(restaurant, key=lambda x: (x[0][0], -int(x[0][1])))
for j in range(N):
    print(resta_new[j][1])
