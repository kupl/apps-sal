# cook your code here
n, sx, sy, ex, ey = map(int, input().split(' '))

reqx = ex - sx
reqy = ey - sy

# // print reqx

str = input()

for i in range(n):
    if reqx < 0:
        if str[i] == 'W':
            reqx += 1

    if reqy < 0:
        if str[i] == 'S':
            reqy += 1

    if reqx > 0:
        if str[i] == 'E':
            reqx -= 1
    if reqy > 0:
        if str[i] == 'N':
            reqy -= 1
    if reqx == reqy and reqx == 0:
        print(i + 1)
        return
print(-1)
