s = input().split(",")
res = ""
for i in range(2):
    res += s[i] + " "

res += s[-1]
print(res)
