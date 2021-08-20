def subseq(a, b):
    j = 0
    for i in range(len(a)):
        if j < len(b) and a[i] == b[j]:
            j = j + 1
    if j == len(b):
        return True
    else:
        return False


s = input()
t = input()
ans = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        cur = s[:i] + s[j + 1:len(s)]
        if subseq(cur, t) and j - i + 1 > ans:
            ans = j - i + 1
print(ans)
