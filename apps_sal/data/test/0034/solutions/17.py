(zh, nh, mmm) = list(map(int, input().split()))
asss = 0
for i in range(1, zh):
    asss = max(asss, min(nh / (zh - i), mmm / i))
print(int(asss // 1))
