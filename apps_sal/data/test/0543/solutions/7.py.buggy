n = int(input())
arr = [int(x) for x in input().split()]

crr = []
hap = 0
for x in arr:
    if(x == 0):
        crr.append(hap)
        hap = 0
    else:
        hap += x
crr.append(hap)

for x in crr:
    if(x % 2):
        print('NO')
        return
print('YES')
