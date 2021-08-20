I = input
n = int(I())
s = I()
j = r = 0
for i in range(n):
    while j < n and s[i:j] in s[j:]:
        j += 1
    r = max(r, j - i - 1)
print(r)
