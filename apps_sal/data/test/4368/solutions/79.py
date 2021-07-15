integer, base = map(int, input().split())
converted_number = ''
while integer > 0:
    converted_number += str(integer % base)
    integer //= base
print(len(converted_number[::-1]))
