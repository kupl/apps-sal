I = input
n = int(I())
s = I()
j = 1
r = []
for i in range(n):
    while j < n and s[i:j] in s[j:]:
        j += 1
    r.append(j - i - 1)
print(max(r))
