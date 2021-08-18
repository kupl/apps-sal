def gcd(a: int, b: int): return gcd(b, a % b) if b else a


nb = int(input())
s = input()
numbers = [int(i) for i in s.split(" ")]
number = -1

flag = True

op = 0


def count1(s):
    res = 0
    for i in s:
        if i == 1:
            res += 1
    return res


if nb == 1:
    if numbers[0] == 1:
        print(0)
    else:
        print(-1)
else:
    while op < 2010:
        new = []
        for i in range(0, len(numbers) - 1):
            g = gcd(numbers[i], numbers[i + 1])
            if g == 1:
                number = nb + op - count1(numbers)
                numbers = []
                print(number)
                return
            else:
                new.append(g)

        numbers = new
        op += 1

    print(number)
