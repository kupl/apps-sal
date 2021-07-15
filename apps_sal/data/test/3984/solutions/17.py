import sys


for line in sys.stdin:
    lexfirst = '{'
    for c in line[:-1]:
        if lexfirst >= c:
            print('Mike')
            lexfirst = c
        else:
            print('Ann')
    quit()

