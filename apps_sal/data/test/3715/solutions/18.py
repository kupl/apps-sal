n = int(input())
l = list(map(int, input().split()))
output = 1 if l[0] == 0 else 0
u = False
for i in range(1, n):
    if l[i] == 0:
        output += 1
    elif l[i] == l[i - 1] and l[i] != 3:
        output += 1
        l[i] = 0
    elif l[i] == 3:
        if l[i - 1] == 1:
            l[i] = 2
        elif l[i - 1] == 2:
            l[i] = 1
print(output)
