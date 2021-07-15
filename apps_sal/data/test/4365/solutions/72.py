num = int(input())

even_count = num // 2

if num % 2 == 0:
    odd_count = even_count
else:
    odd_count = even_count + 1

print((odd_count * even_count))

