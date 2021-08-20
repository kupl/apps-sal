(n, x) = map(int, input().split())
L = list(map(int, input().split()))
val = 0
count = 1
for l in L:
    val += l
    if val <= x:
        count += 1
print(count)
