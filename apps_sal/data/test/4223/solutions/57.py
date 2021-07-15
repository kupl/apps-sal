N = int(input())
S = input()
tmp, rst = '', []
for i in S:
    if i != tmp:
        rst.append(i)
        tmp = i
print(len(rst))
