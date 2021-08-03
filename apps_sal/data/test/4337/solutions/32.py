N = int(input())
color = list(map(str, input().split()))

pp = 0
wp = 0
gp = 0
yp = 0


for i in range(N):
    if color[i] == 'P' and pp == 0:
        pp += 1
    if color[i] == 'W' and wp == 0:
        wp += 1
    if color[i] == 'G' and gp == 0:
        gp += 1
    if color[i] == 'Y' and yp == 0:
        yp += 1

if (pp + wp + gp + yp) == 3:
    print('Three')
else:
    print('Four')
