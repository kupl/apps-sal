n = int(input())
num = list(map(int, input().split()))
fl = True
used = [False] * 110000
for i in range(n):
    if num[i] == 0:
        used[0] = True
        continue
    if num[i] > i or not used[num[i] - 1]:
        ans = i
        fl = False
        break
    else:
        used[num[i]] = True
if not fl:
    print(ans + 1)
else:
    print(-1)
