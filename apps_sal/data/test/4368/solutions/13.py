(N, K) = map(int, input().split())
power = 1
while True:
    if N < K ** power:
        break
    else:
        power += 1
print(power)
