x = int(input())
m = 100
y = 0
while not(m >= x):
    y += 1
    m += m // 100
print(y)
