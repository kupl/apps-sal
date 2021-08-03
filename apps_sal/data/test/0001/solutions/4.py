def sum_str(y):
    return sum(map(int, str(y)))


x = input()
length = len(x)
bad_answer = str(int(x[0]) - 1) + '9' * (length - 1)
total = sum_str(bad_answer)


if length == 1 or sum_str(x) >= total:
    print(x)
else:
    for i in range(length - 1, 0, -1):
        new_total = 9 * (length - i)
        new_answer = str(int(x[:i]) - 1)
        new_total += sum_str(new_answer)

        if new_total >= total:
            new_answer = new_answer if new_answer != '0' else ''
            print(new_answer + '9' * (length - i))
            break
    else:
        print(bad_answer)
