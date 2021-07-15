x = int(input())
while x % 10 == 0:
    x //= 10

b = []
while x > 0:
    b.append(x % 10)
    x //= 10

pol = True
for i in range(len(b) // 2):
    if b[i] != b[len(b) - i - 1]:
        pol = False
        break
if pol:
    print("YES")
else:
    print("NO")
