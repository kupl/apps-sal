n = int(input())
a = input()
b = a[::-1]
c = [[0 for k in range(n + 1)] for l in range(n + 1)]
m = 0
index = -1
# print(a)
# print(b)
# print(c)
for i in range(n + 1):
    for j in range(n + 1):
        if(i == 0 or j == 0):
            c[i][j] = 0
        elif(a[i - 1] == b[j - 1]):
            c[i][j] = 1 + c[i - 1][j - 1]
            if(c[i][j] > m):
                m = c[i][j]
                index = i
        else:
            c[i][j] = 0

print(m)
print(b[n - index:n - index + m])
# print(c)
# print(index-1)
# print(m)
