N = int(input())
A = [int(x) for x in input().split()]

cnt = {}
if N & 1:
    bit = 1
else:
    bit = 0

for a in A:
    if a & bit:
        ans = 0
        break
    if a in cnt:
        cnt[a] += 1
    else:
        cnt[a] = 1

for key in list(cnt.keys()):
    if key == 0 and cnt[key] != 1:
        ans = 0
        break
    if key != 0 and cnt[key] != 2:
        ans = 0
        break
else:
    ans = 2**(N // 2) % 1000000007
print(ans)
