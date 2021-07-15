n, m, k = [int(c) for c in input().split()]

x, y = [1, 1]

def next_cell(x, y):
    if x % 2 == 1 and y < m:
        return [x, y + 1]
    elif x % 2 == 0 and y > 1:
        return [x, y - 1]
    else:
        return [x + 1, y]

for i in range(1, k):
    x2, y2 = next_cell(x, y)
    print(2, x, y, x2, y2)
    x, y = next_cell(x2, y2)

last = [x, y]

req_len = n*m - (k-1)*2

while len(last) < req_len * 2:
    x, y = next_cell(x, y)
    last.append(x)
    last.append(y)

print(len(last) // 2, ' '.join(map(str,last)))
