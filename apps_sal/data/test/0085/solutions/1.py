import sys

size = [0,0,0,0];
size[0], size[1] = sys.stdin.readline().strip().split()
size[2], size[3] = sys.stdin.readline().strip().split()
for i in range(4):
    size[i] = int(size[i])

totalsize = [size[0]*size[1], size[2]*size[3]]
num = [0, 0, 0, 0, 0, 0, 0, 0] #2s in first dimension of 1, 3s in first...
base = [size[0], size[1], size[2], size[3]]
for i in range(4):
    temp = size[i]
    while (temp%2 == 0):
        num[i*2] += 1
        temp /= 2
for i in range(4):
    temp = size[i]
    while (temp%3 == 0):
        num[i*2+1] += 1
        temp /= 3
for i in range(4):
    base[i] /= pow(2, num[2*i])
    base[i] /= pow(3, num[2*i+1])

total = 0
if float(totalsize[0])/pow(2, num[0]+num[2])/pow(3, num[1]+num[3]) == float(totalsize[1])/pow(2, num[4]+num[6])/pow(3, num[5]+num[7]):
    wh = 0
    if num[5]+num[7] > num[1]+num[3]:
        wh = 1
    while (num[wh*4+1]+num[wh*4+3] > num[(wh+1)%2*4+1]+num[(wh+1)%2*4+3]):
        if num[wh*4+1] > 0:
            num[wh*4+1] -= 1
            num[wh*4] += 1
        else:
            num[wh*4+3] -= 1
            num[wh*4+2] += 1
        total += 1
    wh = 0
    if num[4]+num[6] > num[0]+num[2]:
        wh = 1
    while (num[wh*4]+num[wh*4+2] > num[(wh+1)%2*4]+num[(wh+1)%2*4+2]):
        if num[wh*4] > 0:
            num[wh*4] -= 1
        else:
            num[wh*4+2] -= 1
        total += 1
    print(total)
    print(int(base[0]*pow(2, num[0])*pow(3, num[1])), int(base[1]*pow(2, num[2])*pow(3, num[3])))
    print(int(base[2]*pow(2, num[4])*pow(3, num[5])), int(base[3]*pow(2, num[6])*pow(3, num[7])))
else:
    print(-1)


