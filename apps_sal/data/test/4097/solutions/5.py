n = int(input())
b = list(map(int, input().split()))
ind = False
minimum = 10 ** 10
z = [[0, -1, 1], [0, -1, 1]]
if n < 3:
    print(0)
else:
    for i in range(3):
        for j in range(3):
            count = 0
            cnt1 = b[0] + z[0][i]
            cnt2 = b[1] + z[1][j]
            if cnt1 != b[0]:
                count += 1
            if cnt2 != b[1]:
                count += 1
            d = cnt2 - cnt1
            prev = cnt2
            ind1 = True
            for k in range(2, n):
                new_d = b[k] - prev
                if abs(new_d - d) > 1:
                    ind1 = False
                    break
                elif new_d != d:
                    q = d + prev
                    count += 1
                    prev = q
                else:
                    prev = b[k]
            if ind1:
                ind = True
                if count < minimum:
                    minimum = count
    if ind:
        print(minimum)
    else:
        print(-1)
