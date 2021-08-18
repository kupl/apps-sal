
n = int(input())

m = (n + 1) // 2 + (n + 1) % 2

left = n
print(m)
for i in range(1, m + 1):
    if(left == 0):
        break
    print(1, i)
    left -= 1

for i in range(2, m + 1):
    if(left == 0):
        break
    left -= 1

    print(i, m)
