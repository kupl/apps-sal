(n, k) = list(map(int, input().split()))
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
use_chars = chars[:k]
password = ' '
x = 0
for char_i in range(1, n + 1):
    current_char = use_chars[x]
    if password[char_i - 1] == current_char:
        current_char = use_chars[x]
    if x + 1 == k:
        x = 0
    else:
        x += 1
    password += current_char
print(password[1:])
