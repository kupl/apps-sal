from operator import itemgetter
n = int(input())
point = []
ans = []
for i in range(n):
    (a, b) = input().split()
    s = [a, int(b), i + 1]
    point.append(s)
s_point = sorted(point, key=itemgetter(1), reverse=True)
s_point = sorted(s_point, key=itemgetter(0))
[print(s_point[j][2]) for j in range(n)]
