s = []
s = input().split('+')
s.sort()
for i in range(0,len(s)-1,1):
    print(s[i]+'+',end='')
print(s[-1])
