l = [int(input()) for i in range(5)]

diff = 0
num = 0
for i in l:
    if i % 10 == 0:
        num += i
    else:
        a = round(i + 5, -1)
        num += a
        diff = max(diff, a - i)

print(num - diff)
