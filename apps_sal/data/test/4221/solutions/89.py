s = []
s = str(input())


def plural(s):
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')


plural(s)
