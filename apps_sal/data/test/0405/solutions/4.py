n = int(input())
s = input()
ans = 0

for i in s:
    if i == ">":
        break
    ans+=1
for i in s[::-1]:
    if i == "<":
        break
    ans+=1
print(ans)
