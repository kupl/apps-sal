n = int(input())
robo = list(map(int, input().split()))
bionic = list(map(int, input().split()))

only_bionic = sum(1 if b == 1 and robo[i] == 0 else 0 for i, b in enumerate(bionic))
only_robo = sum(1 if r == 1 and bionic[i] == 0 else 0 for i, r in enumerate(robo))
if only_robo == 0:
    print(-1)
    return
cost = only_bionic // only_robo + 1
print(cost)
