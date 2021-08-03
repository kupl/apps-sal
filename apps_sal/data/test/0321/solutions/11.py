t = int(input())
while t > 0:
    a, b = list(map(int, input().split()))
    if a - b != 1:
        print("NO")
    else:
        num = a + b
        num2 = int(num ** 0.5)
        num3 = 2
        ans = 0
        while num3 <= num2:
            if num % num3 == 0:
                ans = 1
            num3 += 1
        if ans == 1:
            print("NO")
        else:
            print("YES")
    t -= 1
