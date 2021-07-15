import sys
n, m = [int(i) for i in input().split()]
a = [[0] * n for i in range(m)]
for i in range(n):
    temp = input()
    for j in range(m):
        a[j][i] = temp[j]

c = 0

def blatant(a):
    for i in range(1,len(a)):
        if a[i] < a[i-1]:
            return True
    return False

match = []
while True:
    if len(a) == 0:
        print(m)
        return
    elif blatant(a[0]):
        del a[0]
        c += 1
    else:
        break

for i in range(1,n):
    if a[0][i] == a[0][i-1]:
        match.append(i)
        
def rm(a,match):
    c = 0
    for m in match:
        i = 1
        while i < len(a):
            if a[i][m] < a[i][m-1]:
                del a[i]
                c += 1
            elif a[i][m] == a[i][m-1]:
                i += 1
            else:
                break
    return c

while True:
    temp = rm(a,match)
    if temp == 0:
        break
    c += temp
    
print(c)

