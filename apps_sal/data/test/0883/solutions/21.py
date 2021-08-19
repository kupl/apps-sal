a = int(input())
b = input().split()
p = 0
for i in range(len(b)):
    p = p + int(b[i])
s = 0
for i in range(1, 6):
    finger = i
    if (p + i) % (a + 1) != 1:
        s = s + 1
print(s)
