import sys
input_file = sys.stdin
C = (10**9+7)
[n, q] = list(int(i) for i in input_file.readline().split())
temp = input_file.readline()
lst = []
for char in temp[:-1]:
    lst.append(int(char))
    
new_lst = [(0, 0)]
for i in lst:
    if i == 0:
        new_lst.append((new_lst[-1][0]+1, new_lst[-1][1]))
    else:
        new_lst.append((new_lst[-1][0], new_lst[-1][1]+1))

ls = [1]
for i in range(n):
    ls.append(ls[-1]*2 % C)

for line in input_file:
    [l, r] = list(int(i) for i in line[:-1].split())
    q = (new_lst[r][0] - new_lst[l-1][0], new_lst[r][1] - new_lst[l-1][1])
    print((ls[sum(q)] - ls[q[0]]) % C)


