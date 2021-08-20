n = int(input())
s = str(input())
s = s.replace('(', ' ( ')
s = s.replace(')', ' ) ')
s = s.replace('_', ' ')
answer = s.split()
a = 0
b = 0
op = False
for element in answer:
    if element == '(':
        op = True
    elif element == ')':
        op = False
    elif op:
        b += 1
    else:
        a = max(len(element), a)
print(a, b)
