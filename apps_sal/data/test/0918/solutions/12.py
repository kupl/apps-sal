student_number, regions = map(int, input().split())
competiton_description = dict()

for _ in range(student_number):
    surname, region, score = input().split()
    if int(region) not in competiton_description:
        competiton_description[int(region)] = [[int(score), surname]]
    else:
        competiton_description[int(region)].append([int(score), surname])

for key, value in sorted(competiton_description.items()):
    value.sort(key=lambda s: (-s[0], s[1]))
    if len(value) > 2 and value[1][0] == value[2][0]:
        print('?')
    else:
        print(value[0][1], value[1][1])
