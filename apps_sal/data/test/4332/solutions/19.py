n = int(input())

sum_digits = 0
for c in str(n):
    sum_digits += int(c)

print(("Yes" if n % sum_digits == 0 else "No"))
