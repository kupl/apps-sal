
inp = input().split(" ")
n = int(inp[0])
k = int(inp[1])

s = set()
for i in range(n):
    a = input().split(' ')
    x = 0
    for j in range(k):
        x = 2 * x + int(a[j])
    s.add(x)

for i in range(16):
    if i in s:
        for j in range(16):
            if j in s:
                if i & j == 0:
                    print("YES")
                    return


print("NO")
