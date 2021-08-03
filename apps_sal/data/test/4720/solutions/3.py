a = int(input())
b = [input().split() for i in range(a)]
c = 0
for i in range(a):
    c = c + (int(b[i][1]) - int(b[i][0]))
print(c + a)
