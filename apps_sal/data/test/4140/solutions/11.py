S = input()
temp = 0

for i in range(len(S)):
    if S[i] != "0" and i % 2 == 0:
        temp += 1
    if S[i] != "1" and i % 2 == 1:
        temp += 1
ans = temp

temp = 0
for i in range(len(S)):
    if S[i] != "0" and i % 2 == 1:
        temp += 1
    if S[i] != "1" and i % 2 == 0:
        temp += 1
if temp < ans:
    ans = temp

print(ans)
