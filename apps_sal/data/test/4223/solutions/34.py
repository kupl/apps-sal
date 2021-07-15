N = int(input())
S = input()
tmp = ''
ls = []
for i in S:
    if i != tmp:
        ls.append(i)
        tmp = i
print(len(ls))
