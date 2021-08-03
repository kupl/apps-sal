ls = []
for i in range(3):
    ls.append(list(map(int, input().split())))
ans = 'Yes'
if ls[1][1] - ls[1][0] != ls[0][1] - ls[0][0]:
    ans = 'No'
if ls[2][1] - ls[2][0] != ls[0][1] - ls[0][0]:
    ans = 'No'
if ls[1][2] - ls[1][0] != ls[0][2] - ls[0][0]:
    ans = 'No'
if ls[2][2] - ls[2][0] != ls[0][2] - ls[0][0]:
    ans = 'No'
print(ans)
