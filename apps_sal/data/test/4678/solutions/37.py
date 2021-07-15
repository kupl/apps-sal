N = int(input())
A = list(map(int, input().split()))
maxhigh = 0
ans = 0
for i in A:
    if maxhigh> i:
        ans += maxhigh - i
    else:
        maxhigh = i
print(ans)
