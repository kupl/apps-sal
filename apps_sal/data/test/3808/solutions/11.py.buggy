n = int(input())
s = input()

depth = 0
ig = False
for i in range(n):
    if(not ig and s[i] == ')'):
        ig = True
        continue
    if(s[i] == '('):
        depth += 1
    else:
        depth -= 1
    if(depth < 0):
        print('No')
        return
if(ig):
    depth -= 1

if(depth):
    print('No')
else:
    print('Yes')
