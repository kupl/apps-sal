colors = list(map(int, input().split()))
faces = {}
faces['top'] = colors[:4]
faces['front'] = colors[4:8]
faces['bottom'] = colors[8:12]
faces['left'] = colors[12:16]
faces['right'] = colors[16:20]
faces['back'] = [colors[21], colors[20], colors[23], colors[22]]
status = {}
for face in list(faces.keys()):
    colors = faces[face]
    if max(colors) == min(colors):
        status[face] = 'ok'
    elif colors[0] == colors[1] and colors[2] == colors[3]:
        status[face] = 'h'
    elif colors[0] == colors[2] and colors[1] == colors[3]:
        status[face] = 'v'
    else:
        status[face] = 'bad'
if 'bad' in list(status.values()):
    print('NO')
elif status['top'] == status['bottom'] == 'ok' and status['front'] == status['left'] == status['right'] == status['back'] == 'h':
    if faces['front'][0] == faces['left'][3] and faces['left'][0] == faces['back'][3] and (faces['back'][0] == faces['right'][3]) and (faces['right'][0] == faces['front'][3]) or (faces['front'][0] == faces['right'][3] and faces['right'][0] == faces['back'][3] and (faces['back'][0] == faces['left'][3]) and (faces['left'][0] == faces['front'][3])):
        print('YES')
    else:
        print('NO')
elif status['left'] == status['right'] == 'ok' and status['front'] == status['top'] == status['bottom'] == status['back'] == 'v':
    if faces['front'][0] == faces['top'][3] and faces['top'][0] == faces['back'][3] and (faces['back'][0] == faces['bottom'][3]) and (faces['bottom'][0] == faces['front'][3]) or (faces['front'][0] == faces['bottom'][3] and faces['bottom'][0] == faces['back'][3] and (faces['back'][0] == faces['top'][3]) and (faces['top'][0] == faces['front'][3])):
        print('YES')
    else:
        print('NO')
elif status['front'] == status['back'] == 'ok' and status['left'] == status['right'] == 'v' and (status['top'] == status['bottom'] == 'h'):
    if faces['top'][0] == faces['left'][1] and faces['left'][0] == faces['bottom'][0] and (faces['bottom'][3] == faces['right'][0]) and (faces['right'][3] == faces['top'][3]) or (faces['top'][0] == faces['right'][0] and faces['right'][1] == faces['bottom'][0] and (faces['bottom'][3] == faces['left'][1]) and (faces['left'][0] == faces['top'][3])):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
