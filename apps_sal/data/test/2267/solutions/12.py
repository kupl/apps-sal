from functools import cmp_to_key
print(''.join((sorted((input() for _ in range(int(input()))), key=cmp_to_key(lambda a, b: 1 if a + b > b + a else-1)))))
