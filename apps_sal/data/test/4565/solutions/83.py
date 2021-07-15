n = int(input())
s = input()

li = []
for i in range(n):
    if s[i]=="W":
        li.append(-1)
    else:
        li.append(1)

cumsum = [li[0]]
for i in range(n-1):
    cumsum.append(cumsum[i] + li[i+1])

l = cumsum.index(max(cumsum))
w_to_e = 0
e_to_w = 0

for i in range(n):
    if i < l:
        if li[i]==-1:
            w_to_e += 1
    elif i > l:
        if li[i]==1:
            e_to_w += 1
print(e_to_w + w_to_e)
