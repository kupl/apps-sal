s = str(input())
a = len(s)
x = 2**(a - 1)
x %= 1000000007
y = 0
z = 0
for i in range(a - 1, -1, -1):
    if(s[i] == "1"):
        z += (2**y)
        z %= 1000000007
    y += 1
print((x * z) % 1000000007)
