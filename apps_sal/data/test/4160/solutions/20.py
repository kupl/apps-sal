count = 0
N = int(input())
now = 100
while N > now:
    now += now // 100
    count += 1
print(count)
