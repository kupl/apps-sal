for _ in range(int(input())):
    s = input()
    if len(s) in {s.count('0'), s.count('1')}:
        print(s)
    else:
        print('01' * len(s))

