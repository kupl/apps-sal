a, b = map(int, input().split())

li = list(map(int, input().split()))

sum = 0
for i in li:
    sum += i

if a > sum:
    print(a - sum)
elif a == sum:
    print(0)
else:
    print(-1)
