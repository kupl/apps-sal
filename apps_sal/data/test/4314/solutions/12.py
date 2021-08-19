(h, w) = map(int, input().split())
mat = [input() for i in range(h)]
n = 0
max = h
while n < max:
    if mat[n] == '.' * w:
        mat.pop(n)
        n -= 1
        max -= 1
    n += 1
flag = [True for i in range(w)]
for i in mat:
    for j in range(w):
        if i[j] == '#':
            flag[j] = False
ans = []
for i in mat:
    temp = ''
    for j in range(w):
        if not flag[j]:
            temp += i[j]
    ans.append(temp)
for i in ans:
    print(i)
