from operator import itemgetter

N = int(input())
restaurants = []

for i in range(N):
    arr = input().split()
    restaurants.append((i + 1, arr[0], -int(arr[1])))

restaurants = sorted(restaurants, key=itemgetter(1, 2))

for i in range(N):
    print(restaurants[i][0])
