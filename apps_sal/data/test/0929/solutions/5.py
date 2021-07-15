import sys
input = lambda: sys.stdin.readline().rstrip()
 
h,w=list(map(int,input().split()))
a=[]
for _ in range(h):
    a.append(list(map(int,input().split())))
ans = []
flag = 1
for i in range(h):
    if flag:
        for j in range(w):
            if j == w - 1:
                flag ^= 1
                if i != h - 1 and a[i][j] % 2 == 1: 
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    a[i + 1][j] += 1
            elif a[i][j] % 2 == 1:
                ans.append([i + 1, j + 1, i + 1, j + 2])
                a[i][j + 1] += 1
    else:
        for j in range(w - 1, -1, -1):
            if j == 0:
                flag ^= 1
                if i != h - 1 and a[i][j] % 2 == 1:
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    a[i + 1][j] += 1
            elif a[i][j] % 2 == 1:
                ans.append([i + 1, j + 1, i + 1, j])
                a[i][j - 1] += 1
print((len(ans)))
for i in ans:
    print((*i))

