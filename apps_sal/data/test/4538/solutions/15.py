N, D = (int(x) for x in input().split())
xy = [map(int, input().split()) for _ in range(N)]
num = 0
for x, y in xy:
    if(x**2 + y**2 <= D**2):
        num += 1
print(num)
