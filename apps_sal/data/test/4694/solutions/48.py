home_num = int(input())
house_from = list(map(int, input().split()))
print(max(set(house_from)) - min(set(house_from)))
