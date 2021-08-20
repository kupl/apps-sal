N = int(input())
S = input()
(tmp, rst) = ('', [])
for i in S:
    if tmp != i:
        rst.append(i)
        tmp = i
print(len(rst))
