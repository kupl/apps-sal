
n = int(input())
tab = sorted(list(map(int, input().split())))
cmex = 1
for num in tab:
    if num >= cmex:
        cmex += 1

print(cmex)
