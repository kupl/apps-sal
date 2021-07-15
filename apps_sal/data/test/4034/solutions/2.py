import sys
n = int(input())
s = input()
l1 = [1]*n
l1[0] = 0
prev = s[0]
for i in range(1, n):
    if s[i] >= prev:
        l1[i] = 0
        prev = s[i]
temp = []
for i in range(n):
    if l1[i] == 1:
        temp.append(s[i])
if len(temp) ==0:
    print("YES")
    print(''.join(str(x) for x in l1))
    return
    
prev = temp[0]
for i in range(1, len(temp)):
    if temp[i] < prev:
        print("NO")
        return
    prev = temp[i]
print("YES")
print(''.join(str(x) for x in l1))
