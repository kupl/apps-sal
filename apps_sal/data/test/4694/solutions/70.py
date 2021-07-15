total_house = int(input())
house_coordinate = sorted(list(map(int, input().split())))
print(house_coordinate[total_house - 1] - house_coordinate[0])
