snacks_num, persons = map(int, input().split())

if snacks_num % persons == 0:
    print(0)
else:
    print(1)
