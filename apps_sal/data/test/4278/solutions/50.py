N = int(input())
ans = 0
li = []
for i in range(N):
    s = list(input())
    s.sort()
    li.append(s)
li.sort()
temp = 1
for j in range(N - 1):
    if li[j] == li[j + 1]:
        temp += 1
    else:
        ans += temp * (temp - 1) // 2
        temp = 1
ans += temp * (temp - 1) // 2
print(ans)
