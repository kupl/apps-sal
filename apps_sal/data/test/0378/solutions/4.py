(k, r) = list(map(int, input().split()))
i = 1
while k * i % 10 != r and k * i % 10 != 0:
    i += 1
if k * i % 10 == 0:
    print(i)
else:
    print(i)
