import sys

n, k = map(int, input().split())

if n // k < 3 or k == 1:
    print(-1)
    return

num = 1
output = []
for i in range(k):
    for j in range(2):
        output.append(str(i + 1))
        num = num + 1

l = num + k
for i in range(k):
    output.append(str(i + 1))
    num = num + 1

while num < n + 1:
    output.append("1")
    num = num + 1

print(" ".join(output))
