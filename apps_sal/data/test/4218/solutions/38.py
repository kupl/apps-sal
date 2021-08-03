n = int(input())

m = n // 2
l = n - m
answer = l / n

if n == 1:
    print(1)
else:
    print(answer)
