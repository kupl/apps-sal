n = input()
string = """0   zero    10  ten     20 twenty 
1   one 11  eleven       
2   two 12  twelve
3   three   13  thirteen    30  thirty
4   four    14  fourteen    40  forty
5   five    15  fifteen         50  fifty
6   six 16  sixteen         60  sixty
7   seven   17  seventeen   70  seventy
8   eight   18  eighteen    80  eighty
9   nine    19  nineteen        90      ninety """

Set = string.split()
#print (Set)
numbers = dict(zip(Set[0::2], Set[1::2]))
if n in numbers:
    print (numbers[n])
else:
    n = int(n)
    print (numbers[str(n // 10 * 10)], '-', numbers[str(n % 10)], sep = '')
