n = int(input())
s = input()
ind = "U"
ans = 0
if s[0] == "R":
    ind = "R"
countr = 0
countu = 0
for i in s:
    if i == "R":
        countr += 1
    else:
        countu += 1
    if ind == "U" and countr > countu:
        ind = "R"
        countr, countu = 1, 0
        ans += 1
    elif ind == "R" and countu > countr:
        ind = "U"
        countu, countr = 1, 0
        ans += 1
print(ans)
