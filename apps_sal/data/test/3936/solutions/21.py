n = int(input())
s1 = list(input())
s2 = list(input())
ans = 0
if s1[0] == s2[0]:
    ans = 3
else:
    ans = 6
for i in range(n - 1):
    if s1[i] == s2[i]:
        ans *= 2
    elif s1[i] == s1[i + 1]:
        continue
    elif s1[i + 1] != s2[i + 1]:
        ans *= 3
    else:
        ans *= 1
print(ans % 1000000007)
