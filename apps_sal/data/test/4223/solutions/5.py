n = int(input())
slimes = input()
fusion = [slimes[0]]

cnt = 0

for i in range(1, n):
    if fusion[cnt] != slimes[i]:
        fusion.append(slimes[i])
        cnt += 1

print(cnt + 1)
