str1 = input().split()
n = int(str1[0])
k = int(str1[1])
q = int(str1[2])

friends = list([int(x) for x in input().split()])
online = set()

for i in range(q):
    str1 = input().split()
    if str1[0] == '2':
        if int(str1[1]) in online:
            print("YES")
        else:
            print("NO")
    else:
        online.add(int(str1[1]))
        if len(online) > k:
            minelem = int(str1[1])
            for on in online:
                if friends[on - 1] < friends[minelem - 1]:
                    minelem = on
            online.remove(minelem)
