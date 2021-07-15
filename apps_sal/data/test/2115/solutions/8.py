stk = []
n = input()
n = int(n)
lst = input()
lst = lst.split()

for a in lst:
    stk.append(int(a))
    while len(stk) > 1:
        if stk[-1] == stk[-2]:
            b = stk[-1]
            stk.pop()
            stk.pop()
            stk.append(b + 1)
        else:
            break
print(len(stk))
for a in stk:
    print(a , end=" ")

