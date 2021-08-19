(n, a, b) = map(int, input().split())
num = list(map(int, input().split()))
x = num.pop(0)
num.sort()
sum1 = sum(num)
num.reverse()
if x * a / (sum1 + x) >= b:
    print(0)
else:
    for i in range(len(num)):
        sum1 -= num[i]
        if x * a / (sum1 + x) >= b:
            print(i + 1)
            break
