import sys

n, m = list(map(int, input().split()))

a = []
for _ in range(m):
    a.append(set(map(int, input().split()[1:])))

for i in a:
    for j in i:
        if -j in i:
            break
    else:
        print("YES")
        return
print("NO")

