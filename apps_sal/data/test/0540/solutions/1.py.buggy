n, m = (int(x) for x in input().split())
mp = [[""]] * n
for i in range(n):
    mp[i] = list(input().strip())

x0, y0 = (int(x) for x in input().split())
x0 -= 1
y0 -= 1
x1, y1 = (int(x) for x in input().split())
x1 -= 1
y1 -= 1


def gen_neighbours(x, y):
    res = []
    if x > 0:
        res.append((x - 1, y))
    if x < n - 1:
        res.append((x + 1, y))
    if y > 0:
        res.append((x, y - 1))
    if y < m - 1:
        res.append((x, y + 1))
    return res


cnt = 0
for el in gen_neighbours(x1, y1):
    if mp[el[0]][el[1]] == '.' or el == (x0, y0):
        cnt += 1


if x0 == x1 and y0 == y1:
    if cnt > 0:
        print("YES")
    else:
        print("NO")
    return

if mp[x1][y1] == "." and cnt <= 1:
    print("NO")
    return

ind = 0
end = 1
q = [0] * (n * m * 2)
q[0] = (x0, y0)

while True:
    if ind == len(q) or q[ind] == 0:
        break

    x, y = q[ind]
    if (x, y) == (x1, y1):
        print("YES")
        return

    for el in gen_neighbours(x, y):
        if el == (x1, y1):
            print("YES")
            return

        if mp[el[0]][el[1]] == '.':
            q[end] = el
            end += 1
            mp[el[0]][el[1]] = 'X'
    ind += 1

print("NO")
