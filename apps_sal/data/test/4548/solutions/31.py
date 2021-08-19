a = input().split()
N = int(a[0])
M = int(a[1])
X = int(a[2])
ryokinjo = []
b = input().split()
for i in range(len(b)):
    ryokinjo.append(int(b[i]))
count1 = 0
count2 = 0
for i in range(len(ryokinjo)):
    if ryokinjo[i] < X:
        count1 += 1
    if ryokinjo[i] > X:
        count2 += 1
print(min([count1, count2]))
