n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[1])
time = 0
ans = "Yes"
for i in range(n):
    time += ab[i][0]
    if time <= ab[i][1]:
        continue
    else:
        ans = "No"
        break
print(ans)
