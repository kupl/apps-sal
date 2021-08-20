visited = []
for _ in range(int(input())):
    s = input()
    if s in visited:
        print('YES')
    else:
        visited.append(s)
        print('NO')
