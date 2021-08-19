A = input()
B = input()
if int(A) == len(B):
    x = ''
    for i in B:
        x += i
        if x[-3:] == 'fox':
            x = x[0:len(x) - 3]
    print(len(x))
