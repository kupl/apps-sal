x, y, x0, y0 = tuple(map(int, input().split()))
s = input()
l = len(s)
res = [0] * (l + 1)
location = [x0, y0]
movement = {tuple(location)}
for i in range(1, l + 1):
    let = s[i - 1]
    if let == 'L':
        if location[1] - 1 > 0:
            location[1] -= 1
    if let == 'R':
        if location[1] + 1 <= y:
            location[1] += 1
    if let == 'U':
        if location[0] - 1 > 0:
            location[0] -= 1
    if let == 'D':
        if location[0] + 1 <= x:
            location[0] += 1
    if tuple(location) in movement:
        res[i] = 0
    else:
        res[i] = 1
    movement.add(tuple(location))
res[0] = 1


res[l] += x * y - sum(res)


print(' '.join(list(map(str, res))))
