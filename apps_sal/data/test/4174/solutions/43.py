x, y = list(map(int, input().split()))
num_list = list(map(int, input().split()))

i = 1
distance = 0
for _ in num_list:
    distance += _
    if distance > y:
        break
    i += 1

print(i)
