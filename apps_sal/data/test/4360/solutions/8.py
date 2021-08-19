a = int(input())
f = list(map(int, input().split()))
bunbo = 0
for i in range(len(f)):
    bunbo += 1 / f[i]
print(1 / bunbo)
