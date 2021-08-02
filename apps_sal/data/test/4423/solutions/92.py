n = int(input())
restaurants = []
for i in range(n):
    s, p = input().split()
    restaurants.append((s, int(p)))
sorted_list = sorted(restaurants, key=lambda x: x[1], reverse=True)
sorted_list.sort(key=lambda x: x[0])

for i in range(n):
    print(restaurants.index(sorted_list[i]) + 1)
