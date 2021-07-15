N = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

# if N == 1: #最初の1区間だけ
#     if t[0] % 2 == 1: #奇数秒
#         if t[0]/2 < v[0]:
#             print ((t[0]/2) ** 2)
#             return
        

# print ('t', t)
# print ('v', v)
N_INF = - 10 ** 15
DP = [[N_INF] * (102) for _ in range(100 * 200 + 2)] #DP[T][V] := 時刻Tに速度Dで走っているときの時刻Tまでの走行距離の最大値
DP[0][0] = 0
# print (DP[0][0:5])
time = 1
for i in range(N):
    # print (i)
    # print ('time', time)
    for j in range(time, time + t[i]): #時刻
        # print (j, end = ' ')
        for k in range(0, v[i] + 1): #速度
            if k == 0: #速度0-->加速して速度0になることはない
                # print (j, k)
                # print (max(DP[j - 1][0], DP[j - 1][1] +  1/2))
                DP[j][k] = max(DP[j - 1][0] + 0.25, DP[j - 1][1] + 1/2)
            elif k != v[i]: #加速してくるときも減速してくることもある
                DP[j][k] = max(DP[j - 1][k -1] + k - 1/2, DP[j - 1][k] + k + 0.25, DP[j - 1][k + 1] + k + 1/2)
            else: #(k == v[i] and j != time) #減速してくることはない
                DP[j][k] = max(DP[j - 1][k -1] + k - 1/2, DP[j - 1][k] + k)
        # print (DP[j][0:5])
    time += t[i]
# print (time)
print((DP[time - 1][0]))
# print ('T = 6, V = 6', DP[6][6])
# print ('T = 12, V = 2', DP[12][2])
# print ('T = 12, V = 3', DP[12][3])
# print ('T = 13, V = 2', DP[13][2])
# print ('T = 26 V = 2', DP[26][2])
# print ('T = 27 V = 2', DP[27][2])

