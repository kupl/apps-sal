n = int(input())
a = list(map(int, input().split()))
good = 0
ans = 0
for x in a:
    if (x >= 4):
        good += 1
    else:
        good = 0
    if (good == 3):
        good = 0
        ans += 1
print(ans)
