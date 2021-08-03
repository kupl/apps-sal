def gns():
    return list(map(int, input().split()))


t = int(input())
for i in range(t):
    if i % 2 == 0:
        s = 'WB' * (t // 2) + 'W' * (t % 2)
    else:
        s = 'BW' * (t // 2) + 'B' * (t % 2)
    print(s)
