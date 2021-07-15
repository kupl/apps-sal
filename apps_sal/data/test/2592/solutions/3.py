from itertools import permutations
for _ in range(int(input())):
    ans = 0
    a, b, c = list(map(int, input().split()))
    for x, y, z in permutations((a, b, c)):
        cnt = 0
        if x:
            cnt += 1
            x -= 1
        if y:
            cnt += 1
            y -= 1
        if z:
            cnt += 1
            z -= 1
        if x and y:
            x -= 1
            y -= 1
            cnt += 1
        if y and z:
            y -= 1
            z -= 1
            cnt += 1
        if x and z:
            x -= 1
            z -= 1
            cnt += 1
        if x and y and z:
            cnt += 1

        ans = max(ans, cnt)

    print(ans)

