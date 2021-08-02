n, A, B, C = map(int, input().split())
r = [A, B, C]
g = list()
for i in range(n):
    g.append(str(input()))


def re(string):
    if string == "AB":
        return(0, 1)
    elif string == "AC":
        return(0, 2)
    else:
        return(1, 2)


def al(num):
    if num == 0:
        return "A"
    elif num == 1:
        return "B"
    else:
        return "C"


flag = 0
result = list()
for i in range(n):
    a, b = re(g[i])
    if r[a] == 0 and r[b] == 0:
        print("No")
        flag = 1
        break
    elif r[a] > r[b]:
        r[a] -= 1
        r[b] += 1
        result.append(al(b))
    elif r[a] < r[b]:
        r[a] += 1
        r[b] -= 1
        result.append(al(a))
    else:
        if i + 1 == n:
            r[a] += 1
            r[b] -= 1
            result.append(al(a))
            break
        x, y = re(g[i + 1])
        if (x, y) == (a, b):
            r[a] += 1
            r[b] -= 1
            result.append(al(a))
        else:
            if x in (a, b):
                r[x] += 2
                r[a] -= 1
                r[b] -= 1
                result.append(al(x))
            else:
                r[y] += 2
                r[a] -= 1
                r[b] -= 1
                result.append(al(y))

if flag == 0:
    print("Yes")
    for item in result:
        print(item)
