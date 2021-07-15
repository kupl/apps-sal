h,w = list(map(int,input().split()))
n = int(input())
ls = list(map(int,input().split()))
di = []
def split_list(l, n):
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]
for i in range(n):
    for j in range(ls[i]): 
        di.append(i+1)
new = list(split_list(di, w))
for j in range(len(new)):
    if j % 2 == 0:
        new[j].sort(reverse=True)
for k in range(len(new)):
    print((*new[k]))

