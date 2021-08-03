for t in range(int(input())):
    s = input()
    print(''.join([s[i] for i in range(len(s)) if i % 2 == 0] + [s[-1]]))
