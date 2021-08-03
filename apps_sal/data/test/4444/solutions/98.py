s, t = list(map(str, input().split()))
ans_str = ""
for i in range(0, len(t)):
    ans_str += t[i]

ans_str1 = ""
for j in range(0, len(s)):
    ans_str1 += s[j]

print(ans_str + ans_str1)
