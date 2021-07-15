n = int(input())

restaurant = []

for i in range(n):
    score_list = input().split()
    score_list.append(i+1)
    score_list[1] = int(score_list[1])
    restaurant.append(score_list)

for l in sorted(restaurant, key=lambda x: (x[0], -x[1])):
    print(l[2])
