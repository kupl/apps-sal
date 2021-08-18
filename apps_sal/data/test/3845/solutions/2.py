A, B = list(map(int, input().split()))
MAX = 100
ans = []
for i in range(MAX):
    if i < MAX // 2:
        temp = ["."] * MAX
    else:
        temp = ["
    ans.append(temp)
A -= 1
B -= 1
h= 0
w= 0
for j in range(B):
    ans[h][w]= "
    w += 2
    if w > MAX - 1:
        h += 2
        w= 0

h= MAX // 2 + 1
w= 0
for j in range(A):
    ans[h][w]= "."
    w += 2
    if w > MAX - 1:
        h += 2
        w= 0
L= [MAX, MAX]
print((*L))
for i in range(MAX):
    output= "".join(ans[i])
    print(output)
