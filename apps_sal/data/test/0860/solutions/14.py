n = int(input())
a = list(map(int, input().split()))
dic = [[] for i in range(n)]

for i, item in enumerate(a, start=1):
    dic[item].append(i)

if not dic[0]:
    print("Impossible")
    return
route = [dic[0].pop()]
s = 0

for i in range(1, n):
    s += 1
    while s >= 0:
        if dic[s]:
            route.append(dic[s].pop())
            break
        else:
            s -= 3
    else:
        print("Impossible")
        return

if len(route) == n:
    print("Possible")
    print(' '.join(str(i) for i in route))
else:
    print("Impossible")
