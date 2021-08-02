n = int(input())
blst = list(map(int, input().split()))
alst = [blst[0]]
for i in range(n - 2):
    alst.append(min(blst[i], blst[i + 1]))
alst.append(blst[-1])
print(sum(alst))
