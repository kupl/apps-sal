n = int(input())
s = input().split(' ')
a,b = input().split(' ')
a = int(a)
b = int(b)
if a>b :
    temp = a
    a = b
    b = temp
count1 = 0
count2 = 0
for i in range(a-1,b-1) :
    count1 += int(s[i])
    s[i] = '0'
for i in s :
    count2 += int(i)
if count1>count2 :
    print(count2)
else :
    print(count1)

