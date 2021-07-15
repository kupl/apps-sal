s = input()
n = len(s)
ans  = 0
for i in range(n):
    for j in range(i, n):
        a = s[i : j + 1]
        b = ""
        for item in a:
            b = item + b
        if (a != b):
            ans = max(ans, len(a))
print(ans)
