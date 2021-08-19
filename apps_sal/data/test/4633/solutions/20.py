for tc in range(int(input())):
    (n, s) = [int(x) for x in input().split()]
    sumOf = sum((int(x) for x in str(n)))
    cost = 0
    carry = False
    for (pos, char) in enumerate(reversed('0' + str(n))):
        if sumOf <= s:
            break
        digit = int(char)
        if carry:
            digit += 1
        if digit != 0:
            carry = True
            cost += (10 - digit) * 10 ** pos
            sumOf -= digit - 1
    print(cost)
