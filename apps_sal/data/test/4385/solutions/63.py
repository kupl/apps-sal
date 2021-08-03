dis = [0 for i in range(5)]
for i in range(5):
    dis[i] = int(input())
k = int(input())

if dis[4] - dis[0] > k:
    print(':(')
else:
    print('Yay!')
