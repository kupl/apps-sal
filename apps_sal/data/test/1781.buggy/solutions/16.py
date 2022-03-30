(n, k) = (int(x) for x in input().split())
plane = []
neig = [[0] * 12 for x in range(n)]
count = [0, 0, 0]
count_all = 0
for i in range(n):
    s = input()
    plane.append(s)
    for j in range(12):
        if s[j] == 'S':
            if j > 0 and (s[j - 1] == 'S' or s[j - 1] == 'P'):
                count_all += 1
            if j < 11 and (s[j + 1] == 'S' or s[j + 1] == 'P'):
                count_all += 1
        if s[j] == '.':
            c = 2
            if j > 0 and s[j - 1] != 'S' or j == 0:
                c -= 1
            if j < 11 and s[j + 1] != 'S' or j == 11:
                c -= 1
            count[c] += 1
            neig[i][j] = c
k1 = k
for i in range(3):
    if k1 >= count[i]:
        (k1, count[i]) = (k1 - count[i], count[i])
    else:
        (k1, count[i]) = (0, k1)
print(count_all + count[1] + 2 * count[2])
for i in range(n):
    for j in range(12):
        if plane[i][j] == '.':
            if k > 0:
                if count[0] > 0 and neig[i][j] == 0:
                    plane[i] = plane[i][:j] + 'x' + plane[i][j + 1:]
                    count[0] -= 1
                    k -= 1
                elif count[1] > 0 and neig[i][j] == 1:
                    plane[i] = plane[i][:j] + 'x' + plane[i][j + 1:]
                    count[1] -= 1
                    k -= 1
                elif count[2] > 0 and neig[i][j] == 2:
                    plane[i] = plane[i][:j] + 'x' + plane[i][j + 1:]
                    count[2] -= 1
                    k -= 1
            else:
                break
    print(plane[i])
