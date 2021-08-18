n = int(input())
s = input()
if n == 1:
    print("YES")
    print(s)
    return
a = []
b = []
for i in range(26):
    a.append(0)
    b.append(-1)
for i in range(len(s)):
    a[ord(s[i]) - ord('a')] += 1
    if b[ord(s[i]) - ord('a')] == -1:
        b[ord(s[i]) - ord('a')] = i
    #print(s[i], i)
num = 0
c = []
for i in range(26):
    if a[i] != 0:
        num += 1
        c.append(b[i])
# print(c)
i = 0
lastNum = 0
if num < n:
    print("NO")
else:
    print("YES")
    minNum = 100000
    for i in range(len(c)):
        if minNum > c[i]:
            minNum = c[i]
            minNumPos = i
    if c[minNumPos] != 0:
        print(s[:c[minNumPos]])
        lastNum = c[minNumPos]
        n -= 1
    c[minNumPos] = 100000
    while n > 1:
        minNum = 100000
        for i in range(len(c)):
            if minNum > c[i]:
                minNum = c[i]
                minNumPos = i
        print(s[lastNum:c[minNumPos]])
        lastNum = c[minNumPos]
        c[minNumPos] = 100000
        #print(c, lastNum)
        n -= 1
    print(s[lastNum:])
    #print(c, lastNum)
# if num >= n:


#print(a, b)
