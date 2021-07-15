input()
n = input()
i = 0
k = 0
for i in range(len(n)):
    if n[i] == "<":
        k+=1
    else:
        break
for i in range(len(n) - 1, -1, -1):
    if n[i] == ">":
        k+=1
    else:
        break
print(k)
