N = int(input())
restaurants = []
for i in range(N):
    name, rating = input().split()
    restaurants.append([name, -int(rating), i])
restaurants.sort()
for i in restaurants:
    print((i[2] + 1))
