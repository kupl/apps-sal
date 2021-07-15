s = input()
l = 0
r = s.count(')')
result = []
for i,c in enumerate(s):
    if c == '(':
        if l<r:
            result.append(i+1)
        l += 1
    else:
        if l>=r:
            result.append(i+1)
        r -= 1
if len(result)>0:
    print(1)
    print(len(result))
    print(*result)
else:
    print(0)

