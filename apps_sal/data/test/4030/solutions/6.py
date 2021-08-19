n = int(input())
s = list(map(ord, input()))
b = [0 for i in range(26)]
ans = []
for i in s:
    for j in range(26):
        if b[j] <= i:
            b[j] = i
            ans.append(j + 1)
            break
print(26 - b.count(0))
print(*ans)
