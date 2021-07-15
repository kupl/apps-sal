no_tree = int(input())
len_tree = []
for i in range(no_tree):
    len_tree.append(int(input()))
time = 0
if len(len_tree) == 1:
    time=len_tree[0] + 1
else:
    for i in range(no_tree-1):
        if i== 0 :  
            time += len_tree[i]+1
        if len_tree[i] <= len_tree[i+1]:
             time += abs(len_tree[i]-len_tree[i+1])+2
             
        elif len_tree[i] > len_tree[i+1]:
             time += abs(len_tree[i]-len_tree[i+1])+2
         
print(time)
