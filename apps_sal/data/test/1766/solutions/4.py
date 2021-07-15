n = input()
line = list(map(int, input().split()))
sum = [0, 0]
player = 1
while len(line) > 0:
    if line[0] > line[-1]:
        sum[player] += line[0]
        player = not player
        line.remove(line[0])
    else:
        sum[player] += line[-1]
        player = not player
        line.remove(line[-1])
print(sum[1], sum[0])
