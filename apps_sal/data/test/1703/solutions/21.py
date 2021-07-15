#This code sucks, you know it and I know it.  
#Move on and call me an idiot later.

def check(symbolString):
    s = []
    tcnt = 0
    balanced = True
    index = 0
    while index < len(symbolString):
        symbol = symbolString[index]
        if symbol == "(":
            s.append(symbol)
        else:
            if len(s) == 0:
                balanced = False
                tcnt += 1
            else:
                s.pop()

        index = index + 1

    if balanced and len(s) == 0:
        return ("()", True)
    else:
        if len(s) > 0 and tcnt > 0:
            return (")(", ")(")
        else:
            if len(s) > 0:
                return ('(', len(s))
            else:
                return(')', tcnt)

n = int(input())

op = {}
cl = {}
b = 0
for i in range(n):
    a = input()
    x = check(a)
    # print(x)
    if x[0] == "()":
        b += 1
    elif x[0] == '(':
        if x[1] in op:
            op[x[1]] += 1
        else:
            op[x[1]] = 0
            op[x[1]] += 1
    else:
        if x[1] in cl:
            cl[x[1]] += 1
        else:
            cl[x[1]] = 0
            cl[x[1]] += 1

b = b ** 2

for i in op: 
    if i in cl:
        b += op[i] * cl[i]

print(b)
