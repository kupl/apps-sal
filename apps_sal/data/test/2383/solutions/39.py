N = int(input())

a = map(int, input().split())

count = 0
for i in a:
    if i == count + 1:
        count += 1
if count != 0:
    print(N - count)
else:
    print('-1')
