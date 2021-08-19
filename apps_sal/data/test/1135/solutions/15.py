n = int(input())
s = input().strip()

# n = 5
# s = 'logva'

# n = 4
# s = 'nfio'

# n = 2
# s = 'no'

# n = 4
# s = 'abba'

assert(len(s) == n)

ans = [None] * n

i = 0

if n % 2 == 1:
    ans[n // 2] = s[0]
    i += 1

    left = n // 2 - 1
    right = n // 2 + 1
else:
    left = n // 2 - 1
    right = n // 2

is_left = True

while i < n:
    ans[left if is_left else right] = s[i]

    if is_left:
        left -= 1
    else:
        right += 1

    is_left = not is_left
    i += 1

# print(ans)
print(''.join(ans))
