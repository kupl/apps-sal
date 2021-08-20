ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
a = [0] * 10
initial = []
n = int(input())
for i in range(n):
    s = input()
    initial.append(s[0])
    for j in range(len(s)):
        a[ch.index(s[j])] += 10 ** (len(s) - j - 1)
sum = 0
flag = False
count = 1
for k in range(10):
    maxFreq = 0
    for l in range(10):
        if maxFreq < a[l]:
            maxFreq = a[l]
    temp = a.index(maxFreq)
    currChar = ch[temp]
    a[temp] = 0
    if currChar not in initial and (not flag):
        flag = True
    else:
        sum += maxFreq * count
        count += 1
print(sum)
