# cook your dish here
def cal(a, b, s):
    if s == '+':
        print(a + b)
    elif s == '-':
        print(a - b)
    elif s == '*':
        print(a * b)
    else:
        print(a / b)


a = int(input())
b = int(input())
c = input()
cal(a, b, c)
