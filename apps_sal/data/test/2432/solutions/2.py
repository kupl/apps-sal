a = int(input())
ans = 0
if a & (1 << 5):
    ans += 1 << 5
if a & (1 << 4):
    ans += 1 << 0
if a & (1 << 3):
    ans += 1 << 2
if a & (1 << 2):
    ans += 1 << 3
if a & (1 << 1):
    ans += 1 << 1
if a & (1 << 0):
    ans += 1 << 4
print(ans)
