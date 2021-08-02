dontt_use = input()
str_list = list(input().split())
n = map(int, str_list)


def foo(n):
    total = 1
    for number in n:
        total = total * number
        if total > 10**18:
            print('-1')
            return
    print(total)


if '0' in str_list:
    print(0)
else:
    foo(n)
