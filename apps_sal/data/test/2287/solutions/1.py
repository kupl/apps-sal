for i in range(int(input())):
    q = input()
    if '1' in q:
        print(q.rfind('1') - q.find('1') - q.count('1') + 1)
    else:
        print(0)
