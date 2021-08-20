cases = []
test = [60, 90, 108, 120, 135, 140, 144, 150, 156, 160, 162, 165, 168, 170, 171, 172, 174, 175, 176, 177, 178, 179]
num = int(input())
for i in range(num):
    cases.append(int(input()))
for j in range(len(cases)):
    if cases[j] in test:
        print('YES')
    else:
        print('NO')
