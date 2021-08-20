n = input()
string = '0   zero    10  ten     20 twenty \n1   one 11  eleven       \n2   two 12  twelve\n3   three   13  thirteen    30  thirty\n4   four    14  fourteen    40  forty\n5   five    15  fifteen         50  fifty\n6   six 16  sixteen         60  sixty\n7   seven   17  seventeen   70  seventy\n8   eight   18  eighteen    80  eighty\n9   nine    19  nineteen        90      ninety '
Set = string.split()
numbers = dict(zip(Set[0::2], Set[1::2]))
if n in numbers:
    print(numbers[n])
else:
    n = int(n)
    print(numbers[str(n // 10 * 10)], '-', numbers[str(n % 10)], sep='')
