comments = input().split(',')
n = len(comments)
p = [n] * n # place holder for count at each layer
ans = [[] for i in range(n)]
layer = 0

for i in range(0,n, 2):
    com = comments[i]
    sub_count = int(comments[i+1])
    while p[layer] == 0: # move back to the previous layer
        layer -= 1
    p[layer] -= 1 # remove the count
    ans[layer].append(com)
    layer += 1 # move to the next layer
    p[layer] = sub_count
while ans[layer]:
    layer += 1
print(layer)
for sub_ans in ans[:layer]:
    print(*sub_ans)

