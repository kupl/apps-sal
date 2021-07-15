n = int(input())
def sum_digit(x):
    if x < 10:
        return x
    else:
        return x%10 + sum_digit(x//10)

print('No' if n%sum_digit(n) else 'Yes')
