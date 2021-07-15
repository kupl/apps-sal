q = int(input())
for i in range(q):
    string = input()
    arr = []
    current = ''
    for index in range(len(string)):
        if not current:
            current += string[index]
            continue
        if string[index] == current[-1]:
            current += string[index]
        else:
            arr.append(current)
            current = string[index]
    if current:
        arr.append(current)
    answer = set()
    for j in arr:
        if len(j) % 2:
            answer.add(j[0])
    print(''.join(sorted(answer)))

