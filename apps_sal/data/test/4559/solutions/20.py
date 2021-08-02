n = int(input())
mod = 10**18
li = list(map(int, input().split()))
li.sort()
ans = 1
for i in range(n):
    ans *= li[i]
    if ans > mod:
        ans = -1
        break
print(ans)
