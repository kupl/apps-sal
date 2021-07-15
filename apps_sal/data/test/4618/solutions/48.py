s = input()
k = int(input())
se = set()
for i in s:
    se.add(i)
if len(s) > 1:
    for i in range(len(s)-1):
        se.add(s[i]+s[i+1])
if len(s) > 2:
    for i in range(len(s)-2):
        se.add(s[i]+s[i+1]+s[i+2])
if len(s) > 3:
    for i in range(len(s)-3):
        se.add(s[i]+s[i+1]+s[i+2]+s[i+3])
if len(s) > 4:
    for i in range(len(s)-4):
        se.add(s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4])
se = sorted(se)
print(se[k-1])
