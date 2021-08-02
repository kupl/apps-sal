n, m = map(int, input().split())
mat = list(map(int, input().split()))
auction = list(map(int, input().split()))
aucpoint = [mat[i - 1] for i in auction]
aucpoint.sort(reverse=True)
for i in auction:
    mat[i - 1] = 0
s = sum(mat)
for point in aucpoint:
    if s > point:
        s *= 2
    else:
        s += point
print(s)
