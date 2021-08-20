(w, l) = list(map(int, input().split()))
j = list(map(int, input().split()))
ans = sum(j[0:l])
temp = ans
for i in range(1, w - l):
    temp += j[i + l - 1] - j[i - 1]
    ans = min(ans, temp)
print(ans)
