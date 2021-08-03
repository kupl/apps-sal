N = int(input())
s = [input() for i in range(N)]
t = sorted(map(sorted, s))
count = 0
ans = 0
for i in range(N - 1):
    if(t[i] == t[i + 1]):
        count += 1
    else:
        ans += (count * (count + 1)) // 2
        count = 0
if(count > 0):
    ans += (count * (count + 1)) // 2
print(ans)
