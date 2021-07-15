_ = input()
S = input()

needs_right = 0
needs_left = 0

for c in S:
    if c == '(':
        needs_right += 1
    else:
        if needs_right == 0:
            needs_left += 1
        else:
            needs_right -= 1

print(('(' * needs_left + S + ')' * needs_right))


