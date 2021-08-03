li = []
n = int(input())
matrix = [[0 for i in range(n)] for i in range(n)]
for _ in range(n):
    l = input()
    li.append(l)
flag = 0
for i in range(n):
    for j in range(n):
        count = 0
        if(j >= 1):
            if(li[i][j - 1] == 'o'):
                count = count + 1
        if(j < n - 1):
            if(li[i][j + 1] == 'o'):
                count = count + 1
        if(i < n - 1):
            if(li[i + 1][j] == 'o'):
                count = count + 1
        if(i >= 1):
            if(li[i - 1][j] == 'o'):
                count = count + 1
        if(count % 2 != 0):
            flag = 1
            break
            break
if(flag == 0):
    print("YES")
else:
    print("NO")
