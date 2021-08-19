def R():
    return map(int, input().split())


(n, l) = R()
lights = sorted(list(R()))
lights_2 = [0] + lights + [l]
res = [[lights_2[i], lights_2[i + 1]] for i in range(n + 2 - 1)]
MAX = [[0, 0], 0]
for pair in res:
    if pair[0] not in lights or pair[1] not in lights:
        if abs(pair[0] - pair[1]) > MAX[1]:
            MAX = [pair, abs(pair[0] - pair[1])]
    elif abs(pair[0] - pair[1]) / 2 > MAX[1]:
        MAX = [pair, abs(pair[0] - pair[1]) / 2]
print(MAX[1])
