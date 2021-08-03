n = int(input())
L = [int(x) for x in input().split()]
L.append(0)

possib = True
for i in range(n):
    if L[i] < 0:
        possib = False
        break
    if L[i] & 1:
        L[i + 1] -= 1

if L[-1] < 0:
    possib = False

if possib:
    print("YES")
else:
    print("NO")
