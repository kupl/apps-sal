p1 = input().split(' ')
p2 = input().split(' ')
p3 = input().split(' ')
p4 = input().split(' ')
version11 = int(p1[0]) > int(p3[1]) and int(p2[1]) > int(p4[0])
version12 = int(p1[0]) > int(p4[1]) and int(p2[1]) > int(p3[0])
version21 = int(p2[0]) > int(p3[1]) and int(p1[1]) > int(p4[0])
version22 = int(p2[0]) > int(p4[1]) and int(p1[1]) > int(p3[0])
version112 = int(p1[0]) < int(p3[1]) and int(p2[1]) < int(p4[0])
version122 = int(p1[0]) < int(p4[1]) and int(p2[1]) < int(p3[0])
version212 = int(p2[0]) < int(p3[1]) and int(p1[1]) < int(p4[0])
version222 = int(p2[0]) < int(p4[1]) and int(p1[1]) < int(p3[0])
if version11 and version12 or (version21 and version22):
    print('Team 1')
elif (version112 or version122) and (version212 or version222):
    print('Team 2')
else:
    print('Draw')
