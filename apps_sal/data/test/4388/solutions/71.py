# ABC111
# A AtCoder Beginner Contest999
n = list(input())
for i in range(len(n)):
    if n[i] == "1":
        n.pop(i)
        n.insert(i, "9")
    elif n[i] == "9":
        n.pop(i)
        n.insert(i,"1")
print((int("".join(n))))

