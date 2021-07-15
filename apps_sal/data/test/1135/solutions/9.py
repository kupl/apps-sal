n = int(input())
word = input()
new_w = [0] * n

if n % 2 == 1:
    middle = n // 2
    new_w[middle] = word[0]
    for i in range(1, middle + 1):
        new_w[middle - i] = word[2 * i - 1]
        new_w[middle + i] = word[2 * i]
    print("".join(new_w))
else:
    new_w.append("")
    middle = (n + 1) // 2
    new_w[middle] = ''
    for i in range(1, middle + 1):
        new_w[middle - i] = word[2 * i - 2]
        new_w[middle + i] = word[2 * i - 1]
    print("".join(new_w))
