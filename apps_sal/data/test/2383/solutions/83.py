N = int(input())
a = list(map(int, input().split()))
i = 1
count = 0
for j in a:
    if i == j:
        i += 1
    else:
        count += 1
if N == count:
    print(-1)
else:
    print(count)
