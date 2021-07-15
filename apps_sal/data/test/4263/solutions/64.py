moji = str(input())
ans = 0
cans = 0
correct = ["A","C","G","T"]
for i in range(len(moji)):
    if moji[i] in correct:
        cans += 1
        if cans > ans:
            ans = cans
    else:
        if cans > ans:
            ans = cans
        cans = 0
print(ans)

