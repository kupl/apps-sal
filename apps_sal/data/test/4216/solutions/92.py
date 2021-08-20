def make_divisors(n):
    div = []
    for i in range(1, -int(-n ** 0.5 // 1)):
        if n % i == 0:
            div.append(i)
    if n % n ** 0.5 == 0:
        div.append(int(n ** 0.5))
    return div


n = int(input())
a = make_divisors(n)[-1]
b = n // a
print(len(str(b)))
