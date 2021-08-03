def main():
    N, A, B, C = list(map(int, input().split()))
    d = {'A': A, 'B': B, 'C': C}
    l = []
    for _ in range(N):
        s = input()
        l.append(s)
    r = []
    for i in range(N):
        x, y = l[i][0], l[i][1]
        z = 'A'
        for j in d:
            if j not in l[i]:
                z = j
        if d[x] > d[y]:
            d[x] -= 1
            d[y] += 1
            r.append(y)
        elif d[y] > d[x]:
            d[x] += 1
            d[y] -= 1
            r.append(x)
        else:
            if d[x] > 1 or i == N - 1:
                d[x] += 1
                d[y] -= 1
                r.append(x)
            elif set(l[i]) == set(l[i + 1]):
                d[x] += 1
                d[y] -= 1
                r.append(x)
            else:
                x2 = 'A'
                for j in l[i + 1]:
                    if j != z:
                        if j == y:
                            x, y = y, x
                if d[z] > 1:
                    d[x] -= 1
                    d[y] += 1
                    r.append(y)
                else:
                    d[x] += 1
                    d[y] -= 1
                    r.append(x)
            if d[x] < 0 or d[y] < 0 or d[z] < 0:
                return False, r
    return True, r


x, y = main()
if x:
    print('Yes')
    for i in y:
        print(i)
else:
    print('No')
