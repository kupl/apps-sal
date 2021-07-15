a1 = ['oops', 'oops', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
a2 = ['oops', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
n = int(input())
d1, d2 = n // 10, n % 10
if n == 0:
    print('zero')
elif d1 == 0:
    print(a2[d2])
elif d1 == 1:
    if n == 10:
        print('ten')
    elif n == 11:
        print('eleven')
    elif n == 12:
        print('twelve')
    elif n == 13:
        print('thirteen')
    elif n == 14:
        print('fourteen')
    elif n == 15:
        print('fifteen')
    elif n == 16:
        print('sixteen')
    elif n == 17:
        print('seventeen')
    elif n == 18:
        print('eighteen')
    elif n == 19:
        print('nineteen')
else:
    if d2 == 0:
        print(a1[d1])
    else:
        print(a1[d1], a2[d2], sep='-')
