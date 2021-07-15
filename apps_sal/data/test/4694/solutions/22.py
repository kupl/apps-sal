n = input()
data = list(map(int,input().split()))
data.sort(reverse = True)
ans = 0
for i in range(len(data) - 1):
    ans += data[i] - data[i + 1]
print(ans)
