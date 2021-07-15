n,s = open(0).read().split()

imp_close = 0
imp_open = 0

for char in s:
    if char == '(':
        imp_open += 1
    else:
        if imp_open:
            imp_open -= 1
        else:
            imp_close += 1

print('('*imp_close + s + ')'*imp_open)
