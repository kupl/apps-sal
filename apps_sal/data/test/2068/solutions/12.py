result = []
pol = 'polycarp'
for i in range(int(input())):
    point = False
    (new_person, _, was) = [x.lower() for x in input().split()]
    if was == pol:
        result.append([pol, new_person])
    elif was in [x[-1] for x in result]:
        for line in result:
            if line[-1] == was:
                line.append(new_person)
                break
    else:
        for line in result:
            for name in line[1:-1]:
                if name == was:
                    i = line.index(name)
                    new_person_line = line[:i + 1]
                    new_person_line.append(new_person)
                    result.append(new_person_line)
                    point = True
                    break
            if point:
                break
m = max((len(line) for line in result))
print(m)
