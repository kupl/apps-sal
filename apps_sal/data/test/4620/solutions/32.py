N = int(input())
CSF = [[0] * 3 for i in range(N-1)]

for i in range(N-1):
    c, s, f = list(map(int, input().split()))
    CSF[i][0] = c
    CSF[i][1] = s
    CSF[i][2] = f

for i in range(N-1):
    now = CSF[i][1]+CSF[i][0]
    for j in range(i+1, N-1):
        # 1本目の前なら1本目まで待つ
        if now <= CSF[j][1]:
            now += CSF[j][0]+(CSF[j][1]-now)

        # 1本目以降なら待ち時間と移動時間を加算する
        else:
            while (now - CSF[j][1]) % CSF[j][2] != 0:
                now += 1
            now += CSF[j][0]
    print(now)
print((0))

