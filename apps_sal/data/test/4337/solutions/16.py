N = int(input())
S = list(map(str, input().split()))

color = []

for i in S:
    if i in color:
        pass
    else:
        color.append(i)

if len(color) == 4:
    print('Four')
else:
    print('Three')
