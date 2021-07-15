s=[]
for c in input():
     if len(s) and s[-1]==c:
          s.pop()
     else:
          s.append(c)
if len(s):
     print('No')
else:
     print('Yes')
