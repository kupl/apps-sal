N = int(input())

a = map(int, input().split())
A = []
count = 0
for i in a:
    if i == count + 1:
        A.append(i)
        count += 1
if A:
    print(N - count)
else:
    print('-1')
