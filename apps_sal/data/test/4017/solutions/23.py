def main():
    count = int(input())
    arr = input().split(' ')
    store = []
    tot = 0
    biggest = 0
    second_biggest = 0
    index_biggest = 0
    index_second_biggest = 0
    for x in range(count):
        test = int(arr[x])
        store.append(test)
        tot += test
        if test >= biggest:
            (biggest, second_biggest) = (test, biggest)
            (index_biggest, index_second_biggest) = (x, index_biggest)
        elif test > second_biggest:
            second_biggest = test
            index_second_biggest = x
    number = 0
    string = ''
    for x in range(count):
        if store[x] == biggest:
            if tot - store[x] == 2 * second_biggest:
                number += 1
                string += str(x + 1) + ' '
        elif tot - store[x] == 2 * biggest:
            number += 1
            string += str(x + 1) + ' '
    print(number)
    print(string)


main()
