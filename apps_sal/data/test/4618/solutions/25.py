s = input()
k = int(input())
#l = "abcdefghijklmnopqrstuvwxyz"
# print(ord("b")) 97
ans = []
for i in range(len(s)):
    x = 0
    for j in range(5):
        if (i + j < len(s)):
            x += (ord(s[i + j]) - 96) * 10**(8 - 2 * j)
            ans.append((x, s[i:i + j + 1]))
ans = list(set(ans))
ans.sort()
# print(ans)
print(ans[k - 1][1])
