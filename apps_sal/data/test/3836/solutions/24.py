n = int(input())

influences = [[], [], [], []]

for i in range(0, n):
    [support, influence] = [x for x in input().split()]
    support = int(support, 2)
    influences[support].append(int(influence))

for i in range(0, 4):
    influences[i] = sorted(influences[i])
    influences[i].reverse()

total_influence = 0
total_influence += sum(influences[3])

min_size = min(len(influences[2]), len(influences[1]))

total_influence += sum(influences[1][:min_size]) + sum(influences[2][:min_size])

size = len(influences[3])

influences[0] += influences[1][min_size:] + influences[2][min_size:]
influences[0] = sorted(influences[0])
influences[0].reverse()

total_influence += sum(influences[0][:size])

print(total_influence)
