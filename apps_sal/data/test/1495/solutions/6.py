n = int(input())
s = list(map(int, input().split()))
l = [bin(i)[2:] for i in s]
length = [len(i) for i in l]
maxLen = max(length)
minLen = min(length)
loc = 0
flag = False
for j in range(minLen):
    for i in range(n):
        if l[i][j] != l[0][j]:
            flag = True
            break
    if flag:
        break
    loc += 1
result = sum(length) - loc * n
best = result
change = n * [-1]
for j in range(loc, maxLen):
    for i in range(n):
        if j >= length[i] or l[i][j] == '1':
            change[i] = 1
    result += sum(change)
    if result > best:
        break
    best = result
print(best)
