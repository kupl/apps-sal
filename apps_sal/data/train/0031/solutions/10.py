

t = int(input())
for test in range(t):
    s = input()
    v = set()
    start = 0
    ans = 0
    cur = [0, 0, 0, 0]
    for i in s:
        if i == "N":
            cur[2] += 1
        elif i == "S":
            cur[2] -= 1
        elif i == "E":
            cur[3] += 1
        else:
            cur[3] -= 1

        key1 = str(cur)
        key2 = str([cur[2], cur[3], cur[0], cur[1]])
        if key1 in v:
            ans += 1
        else:
            ans += 5

        v.add(key1)
        v.add(key2)

        cur[0] = cur[2]
        cur[1] = cur[3]
    print(ans)
