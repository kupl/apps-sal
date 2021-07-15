n, m = map(int, input().split())
l = [n, m]
r = [-1, -1]
for i in range(n):
    A = input()
    if A.find('*')!=-1:
        if i < l[0]:
            l[0] = i
        if A.find('*') < l[1]:
            l[1] = A.find('*')
        if i > r[0]:
            r[0] = i
        if A.rfind('*') > r[1]:
            r[1] = A.rfind('*')
print(max(r[0]-l[0]+1, r[1]-l[1]+1))
