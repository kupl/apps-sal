n = int(input())
guzai = list(map(int, input().split()))

guzai.sort()

ave = (guzai[0] + guzai[1]) / 2

for x in range(2, n):
    ave = (ave + guzai[x]) / 2

print(ave)
