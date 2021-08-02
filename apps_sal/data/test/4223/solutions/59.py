N = int(input())
S = input()
tmp, val = '', []
for i in S:
    if i != tmp:
        val.append(i)
        tmp = i
print(len(val))
