inp = input()
n = len(inp)//2+1
t = False
for i in range(n,len(inp)):
    if inp[:i] == inp[-i:]:
        t = True
        n = i
        break

if t:
    print("YES")
    print(inp[:n])
else:
    print("NO")
