s = input()

is_correct = True

for fs in range(26):
    for sc in range(fs + 1, 26):
        is_first = s.find(chr(ord('a') + fs))
        is_second = s.find(chr(ord('a') + sc))

        if is_second != -1:
            is_correct &= is_first != -1
            is_correct &= is_first < is_second


print('YES' if is_correct else 'NO')
