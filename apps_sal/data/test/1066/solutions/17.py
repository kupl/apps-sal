x = input().split()
n = int(x[0])
k = int(x[1])

first_even_position = (n+1)//2 + 1
if (k < first_even_position) :
    number = k * 2 - 1
else:
    number = (k - first_even_position + 1) * 2

print(number)
