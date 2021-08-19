nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
string = str(input())
ind = []
for i, char in enumerate(string):
    if char == ".":
        ind.append(i)
flag = 1
# print(ind)
for i in range(len(ind) - 1):
    if ind[i + 1] - ind[i] > k:
        flag = 0
        break
if flag == 1:
    print("YES")
else:
    print("NO")
