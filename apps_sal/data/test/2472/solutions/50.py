N = int(input())
li = []
ans = "Yes"
t = 0
for i in range(N):
    A, B = list(map(int, input().split()))
    li.append([B, A])
li.sort()

for j in range(N):
    t += li[j][1]
    if t <= li[j][0]:
        pass
    else:
        ans = "No"

print(ans)
