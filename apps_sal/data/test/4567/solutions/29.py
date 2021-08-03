N = int(input())
s = [int(input()) for _ in range(N)]

res = 0
other = []

for num in s:
    if num % 10 == 0:
        res += num
    else:
        other.append(num)

if other:
    other.sort()
    res += sum(other)
    if res % 10 == 0:
        res -= other[0]
    print(res)

else:
    print(0)
