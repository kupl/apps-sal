n = int(input())
mass = list(map(int, input().split()))
num = 0
flag = True
for i in range(n):
    if mass[i] == i:
        num += 1
    elif flag and mass[mass[i]] == i:
        num += 2
        flag = False
if flag and num != n:
    num += 1
print(num)
