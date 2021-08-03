n = int(input())
c = 0
r = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        c += 1
        if c == 3:
            print('Yes')
            return
    else:
        c = 0
print('No')
