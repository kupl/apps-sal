def is_subsequence(x, y):
    x = list(x)
    for letter in y:
        if x and x[0] == letter:
            x.pop(0)
    return not x


s = input()
print('YES' if is_subsequence('heidi', s) else 'NO')
