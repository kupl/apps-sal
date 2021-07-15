s = input()
k = int(input())
le = len(s) + k
m = 0
for i in range(len(s)):
    j = 1
    while i+2*j <= le:
        mi = i + j
        la = i + 2*j
        if mi >= len(s):
            m = max(m, j)
        if la <= len(s) and s[i:mi] == s[mi:la]:
            m = max(m, j)
        if mi < len(s):
            xl = len(s) - mi
            if s[i:i + xl] == s[mi:len(s)]:
                m = max(m, j)
        j += 1
print(2*m)

