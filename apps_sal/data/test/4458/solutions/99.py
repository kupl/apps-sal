n = int(input())
num = list(map(int, input().split()))
count = 10**18
ans = 0

for i in num:
    if count > i:
        count = i
        ans += 1

print(ans)
