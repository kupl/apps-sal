n = int(input())
l = list(map(int, input().split()))
j = k = 0
for i in l:
    if i % 2 == 1:
        j += 1
    else:
        k += 1
print(min(j, k))
