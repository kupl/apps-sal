import math
a = [int(input()) for i in range(5)]
sub = 0
cnt = 0
for i in a:
    if i % 10 != 0 and sub < 10 - i % 10:
        sub = 10 - i % 10
    cnt += math.ceil(i / 10) * 10
print(cnt - sub)
