def to_fizzbuzz(number):
    if number % 15 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)


def main():
    N = int(input())
    fblist = []
    for number in range(1, 10 ** 6):
        result = to_fizzbuzz(number)
        fblist.append(result)
    n_list = fblist[0:N]
    n_numlist = []
    for s in n_list:
        if s.isdigit() == True:
            n_numlist.append(int(s))
    print(sum(n_numlist))


main()
