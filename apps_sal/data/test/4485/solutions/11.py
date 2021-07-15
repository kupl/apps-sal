n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ini_1 = []
end_n = []
for i in range(m):
    if ab[i][0] == 1:
        ini_1.append(ab[i][1])
    elif ab[i][1] == n:
        end_n.append(ab[i][0])
if set(ini_1) & set(end_n):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
