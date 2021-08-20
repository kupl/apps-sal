n = int(input())
d = list(map(int, input().split()))
sam = 0
for i in range(n):
    for j in range(i + 1, n):
        sam = sam + d[i] * d[j]
print(sam)
