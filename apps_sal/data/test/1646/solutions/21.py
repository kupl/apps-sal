def mp():
    return map(int, input().split())


#f = open("input.txt","r")
n = int(input())
a = list(input())
if a == ['0']:
    print('0')
else:
    print('1' + '0' * a.count('0'))
