n = int(input())
s = input()
ss = input()
tree = [[1]]
p = list(map(int, s.split()))
q = list(map(int, ss.split()))
for i in range(0, n-1):
    tree.append([i+2])
    tree[p[i]-1].append(i+2)
count = 0
for each in tree:
    if len(each) == 1:
        tree.remove(each)
        count += 1
tree.sort(key=len)
for each in tree:
    sub = list(map(lambda x:q[x-1], each[1:]))
    count += (1-sub.count(q[each[0]-1]))
print(count)
