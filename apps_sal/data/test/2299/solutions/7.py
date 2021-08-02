#---------------EL FUTURO ES INCIERTO--------------#
n, m = [int(x) for x in input().split()]
arr = [[int(x) for x in input().split()]for i in range(0, n)]
p = [i for i in range(0, n + 1)]

for j in range(0, m):
    cur = 0
    for i in range(0, n - 1):
        if(arr[i][j] <= arr[i + 1][j]):
            p[i + 1] = min(cur, p[i + 1])
        else:
            cur = i + 1
    # end for
# end for

q = int(input())
res = ""
for _ in range(0, q):
    a, b = [int(x) for x in input().split()]
    b -= 1
    a -= 1
    if(p[b] <= a):
        res += "Yes"
    else:
        res += "No"
    if _ != q - 1:
        res += "\n"
# end for

print(res)
