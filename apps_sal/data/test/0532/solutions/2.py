s = input()
S = "abcdefghijklmnopqrstuvwxyz"

ind = 0
ans = 0
for item in s:
    index = ind
    ans1 = 0
    while (S[index] != item):
        index = (index + 1) % 26
        ans1 += 1
    index = ind
    ans2 = 0
    while (S[index] != item):
        index = (index - 1 + 26) % 26
        ans2 += 1
    ans += min(ans1, ans2)
    ind = index
print(ans)

