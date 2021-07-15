N = int(input())
my_str = str(N)
my_sum = 0
for i in my_str:
    my_sum += int(i)
print(('Yes' if my_sum % 9 == 0 else 'No'))
