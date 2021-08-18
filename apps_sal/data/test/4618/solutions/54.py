s = input()
k = int(input())

cand = []
for i in range(len(s)):
    temp = ''
    for j in range(k):
        if i + j >= len(s):
            continue
        temp += s[i + j]
        cand.append(temp)

cand.sort()
ans = cand.pop(0)
k -= 1
while k != 0:
    temp = cand.pop(0)
    if temp == ans:
        continue
    ans = temp
    k -= 1

print(ans)
