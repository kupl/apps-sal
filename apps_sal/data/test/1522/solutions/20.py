n = int(input())
s = input().upper()
a = [0] * 26
u = 0
for i in range(len(s)):
    if i % 2 == 0:
        a[ord(s[i]) - ord('A')] += 1
    else:
        if a[ord(s[i]) - ord('A')] > 0:
            a[ord(s[i]) - ord('A')] -= 1
        else:
            u += 1
print(u)
