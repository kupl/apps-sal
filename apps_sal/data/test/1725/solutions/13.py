# http://codeforces.com/problemset/problem/289/B
n,m,d = list(map(int, input().split()))
mat = []
for _ in range(n):
     for x in list(map(int, input().split())):
        mat.append(x)
    #mat.append([x for x in list(map(int, input().split()))])
#print(mat)
x = mat[0] % d
#print(x)
for y in mat:
    if y % d != x:
        print(-1)
        return
mat = [(y-x)/d for y in mat]
#print(mat)
mat.sort()
#print(mat)
med = mat[int((m*n) / 2)]
#print(med)
print(int(sum([abs(y-med) for y in mat])))

