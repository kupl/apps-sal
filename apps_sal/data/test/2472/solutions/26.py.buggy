n = int(input())
t = 0
ab = [list(map(int, input().split())) for i in range(n)]
abt = sorted(ab, key=lambda x: x[1])
for i in range(n):
    t += abt[i][0]
    if t > abt[i][1]:
        print('No')
        return
print('Yes')
