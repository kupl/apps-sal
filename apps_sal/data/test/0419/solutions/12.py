s = input()
ans = len(s) - 1
k = 0
for i in s:
    k += int(i)
if k > 1:
    ans += 1
if ans % 2 != 0:
    ans += 1
print(ans // 2)
