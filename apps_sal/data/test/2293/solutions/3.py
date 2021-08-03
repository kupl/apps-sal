def check(arr1, arr2):
    i1 = 0
    i2 = 0
    while True:
        if i1 == len(arr1) or i2 == len(arr2):
            return False
        elif arr1[i1] == arr2[i2]:
            return True
        elif arr1[i1] < arr2[i2]:
            i1 += 1
        else:
            i2 += 1


m, n = (int(x) for x in input().split())

day___set = []
for i in range(m):
    x = sorted([int(x) for x in input().split()][1:])
    day___set.append(x)

for i in range(m):
    for j in range(i + 1, m):
        if not check(day___set[i], day___set[j]):
            print('impossible')
            quit()
print('possible')
