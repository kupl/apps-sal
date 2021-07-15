l = [list(map(int, input().split())) for i in range(3)]
n = int(input())
s = set([int(input()) for j in range(n)])

ans = "No"

for i in range(3):
    if l[i][0] in s and l[i][1] in s and l[i][2] in s:
        ans = "Yes"

for i in range(3):
    if l[0][i] in s and l[1][i] in s and l[2][i] in s:
        ans = "Yes"

if l[0][0] in s and l[1][1] in s and l[2][2] in s:
    ans = "Yes"
elif l[0][2] in s and l[1][1] in s and l[2][0] in s:
    ans = "Yes"

print(ans)
