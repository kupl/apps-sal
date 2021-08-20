n = int(input())
s = input()
left = 0
right = len(s) - 1
itog = 0
while left < n - 1 and s[left + 1] == s[left]:
    left += 1
while right > 0 and s[right - 1] == s[right]:
    right -= 1
if left < right and s[0] != s[n - 1]:
    itog += left + 1 + 1 + (len(s) - right)
    print(itog % 998244353)
elif left < right and s[0] == s[n - 1]:
    itog += (left + 1 + 1) * (n - right + 1)
    print(itog % 998244353)
else:
    itog = n * (n - 1) // 2 + n
    print(itog % 998244353)
