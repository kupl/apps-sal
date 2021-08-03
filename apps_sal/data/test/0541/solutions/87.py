N, M = map(int, input().split())
warzones = [[] for i in range(M)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    warzones[i] = [a, b]
warzones = sorted(warzones, key=lambda x: x[0])
# print(warzones)
shaku = warzones[0]
cnt = 1
for i in range(1, M):
    # print(shaku)
    # 尺継続条件
    if(warzones[i][0] < shaku[1]):
        shaku[0] = max(warzones[i][0], shaku[0])
        shaku[1] = min(warzones[i][1], shaku[1])
    else:
        cnt += 1
        shaku = warzones[i]

print(cnt)

'''尺取法の初期化
最初に配列のlists[0]で初期化
for i in range(1,M):でまわして
okの場合lists[i]を代入
ngのときはカウントを増やしてngで再初期化
'''
