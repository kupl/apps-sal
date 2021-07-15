n = int(input())
a = list(map(int, input().split()))
count = 1

for i in a:
    if i == count:
        count += 1
if count == 1:
    print(-1)
else:
    print(n - count + 1)
