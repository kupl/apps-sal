ans = 0
position = []
for i in range(5):
    x = int(input())
    position.append(x)
k = int(input())
distance_list = []
for i in range(5):
    for j in range(5):
        if i != j:
            distance = abs(position[i] - position[j])
            distance_list.append(distance)

y = max(distance_list)
if y <= k:
    print('Yay!')
else:
    print(':(')
