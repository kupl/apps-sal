s = input()
k = int(input())
wi = list(map(int, input().split()))
res = 0
for i in range(len(s)):
    res += wi[ord(s[i]) - 97] * (i + 1)
print(res + max(wi) * (k * (k + 1) // 2 + len(s) * k))
