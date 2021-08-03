a = list(map(int, input().rstrip().split()))
out = 0
for i in a:
    if i > 1:
        out += i * (i - 1) // 2
print(out)
