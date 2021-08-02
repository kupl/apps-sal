n, m = list(map(int, input().split()))
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = list(map(int, input().split()))
'''
check = 0


for i in range(m):
    if a[i] == 1:
        check = b[i]
        for j in range(m):
            if a[j] == check and b[j] == n:
                print("POSSIBLE")
                return

print("IMPOSSIBLE")

'''
start = []
leave = []
for i in range(m):
    if a[i] == 1:
        start.append(b[i])
    elif b[i] == n:
        leave.append(a[i])

if set(start) & set(leave):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
