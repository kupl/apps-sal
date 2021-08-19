alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string = input()
numbers = string.split()
(a, b) = (int(numbers[0]), int(numbers[1]))
condition = a > 1 and b == 1
if b > a or condition:
    print(-1)
else:
    if a == 1:
        s = 'a'
    else:
        n = a - b + 2
        s = 'ab' * (n // 2)
        if n % 2 == 1:
            s += 'a'
        for x in range(2, b):
            s += alphabet[x]
    print(s)
