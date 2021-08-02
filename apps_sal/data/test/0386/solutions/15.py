import sys

queries = int(sys.stdin.readline())

opp = {'>': '<=',
       '>=': '<',
       '<': '>=',
       '<=': '>'}

lower = -2000000000
upper = 2000000000

for i in range(queries):
    oper, num, judge = sys.stdin.readline().rstrip().split(' ')
    if judge == 'N':
        oper = opp[oper]

    if oper == '>':
        lower = max(int(num) + 1, lower)
    elif oper == '>=':
        lower = max(int(num), lower)
    elif oper == '<':
        upper = min(int(num) - 1, upper)
    elif oper == '<=':
        upper = min(int(num), upper)
    #print(str(lower) + " " + str(upper))
    if(lower > upper):
        break

if(lower > upper):
    print("Impossible")
else:
    print(lower)
