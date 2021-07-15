n = int(input())
a = list(map(int, input().split()))
minus = 0
sum = 0
zero = False
minimum = abs(a[0])
for i in a:
    if i == 0:
        zero = True
    if i < 0:
        minus += 1
    minimum = min(minimum, abs(i))
    sum += abs(i)
if zero:
    print(sum)
elif minus % 2 == 0:
    print(sum)
else:
    print(sum - 2 * minimum)
