mountain_number = input()
mountain_height = map(int, input().split())
observable_inn = observable_height = 0
for i in mountain_height:
    if i >= observable_height:
        observable_height = i
        observable_inn += 1
print(observable_inn)
