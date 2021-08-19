n = int(input())
for j in input().split():
    i = int(j)
    if i % 2 == 0:
        i -= 1
    print(i, end=' ')
print()
