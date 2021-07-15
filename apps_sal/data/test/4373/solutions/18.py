n = int(input())
l = list(map(int, input().split()))
l.sort(    )
k = 1
for i in l:
    if i >= k:
        k += 1
print(k - 1)
