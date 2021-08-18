num = list(map(int, input().split()))
string = input()
countl = 0
countr = num[1]
i = 0
j = num[0]
L = []
R = []
while countl != num[1]:
    if string[i] == 'o':
        L.append(i + 1)
        countl = countl + 1
        i = i + num[2] + 1
    else:
        i = i + 1
    if i >= num[0]:
        break
while countr != 0:
    if string[j - 1] == 'o':
        R.append(j)
        countr = countr - 1
        j = j - num[2] - 1
    else:
        j = j - 1
    if j < 0:
        break
R.reverse()
for k in range(num[1]):
    if L[k] == R[k]:
        print((L[k]))
