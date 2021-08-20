n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: (-x[1], x[0]))
cd.sort(key=lambda x: (x[0], x[1]))
s = [0] * n
for i in range(n):
    for j in range(n):
        if s[j] == 0 and ab[j][0] < cd[i][0] and (ab[j][1] < cd[i][1]):
            s[j] = 1
            break
print(sum(s))
