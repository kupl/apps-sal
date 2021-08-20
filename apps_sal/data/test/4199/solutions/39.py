(total_people, min_height) = map(int, input().split())
height = map(int, input().split())
rideable_people = 0
for i in height:
    if i >= min_height:
        rideable_people += 1
print(rideable_people)
