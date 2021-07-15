N = int(input())
list = []
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        "FizzBuzz"
    elif i % 3 == 0:
        "Fizz"
    elif i % 5 == 0:
        "Buzz"
    else:
        list.append(i)
print(sum(list))
