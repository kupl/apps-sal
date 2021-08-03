n = int(input())
m = {}
line = list(map(int, input().split()))
for i in line:
    if i != 0:
        m[i] = 1
print(len(m))
