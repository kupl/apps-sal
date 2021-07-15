input()
mas = input()
ans = [0] * len(mas)
stack = 0

maxx = 0

for i in mas:
    if(i == "["):
        stack += 1
    else:
        stack -= 1
    maxx = max(maxx, stack)


stack = []
for i in range(len(mas)):
    if(mas[i] == "["):
        stack.append(i)
    else:
        j = stack.pop()
        ans[i] = len(stack)
        ans[j] = len(stack)


for i in range(len(ans)):
    ans[i] = maxx - ans[i]

    
i = 0
while i != len(ans) - 1:
    if(mas[i] == "[" and mas[i + 1] == "]"):
        mas = mas[:i + 1] + "___" + mas[i + 1:]
        ans.insert(i + 1, "_")
        ans.insert(i + 1, "_")
        ans.insert(i + 1, "_")
        i += 2
    i += 1


for i in range(maxx, 0, -1):
    for x in range(len(ans)):
        if(ans[x] == "_"):
            if(ans[x - 1] == i or ans[x + 1] == i):
                print("-", end = "")
            else:
                print(" ", end = "")
        else:
            if(ans[x] == i):
                print("+", end = "")
            elif(ans[x] > i):
                print("|", end = "")
            elif(ans[x - 1] == i or ans[x + 1] == i):
                print("-", end = "")
            else:
                print(" ", end = "")
    print()


for i in range(0, maxx + 1):
    for x in range(len(ans)):
        if(ans[x] == "_"):
            if(ans[x - 1] == i or ans[x + 1] == i):
                print("-", end = "")
            else:
                print(" ", end = "")
        else:
            if(ans[x] == i):
                print("+", end = "")
            elif(ans[x] > i):
                print("|", end = "")
            elif(ans[x - 1] == i or ans[x + 1] == i):
                print("-", end = "")
            else:
                print(" ", end = "")
    print()
