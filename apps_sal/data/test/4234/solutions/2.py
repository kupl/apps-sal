n = int(input())
s = input() + "K"
count = 0
ans = []
i = 0
while i < n:
    if s[i] == s[i + 1]:
        count += 1
        i += 1
    else:
        ans.append(s[i])
        ans.append(s[i + 1])
        i += 2
if ans[-1] == "K":
    ans.pop()
    ans.pop()
    count += 1
print(count)
print("".join(ans))

