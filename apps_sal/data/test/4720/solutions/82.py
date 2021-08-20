a = int(input())
x = ''
y = 0
for i in range(a):
    x = input().split()
    y += abs(int(x[0]) - int(x[1])) + 1
print(y)
