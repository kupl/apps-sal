s = input()
a = ""
for i in s[::-1]:
    a = i + a
    if a in ["dream", "dreamer", "erase", "eraser"]:
        a = ""
print("NO" if len(a) else "YES")
