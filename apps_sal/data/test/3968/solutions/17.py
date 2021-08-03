n = int(input())
a = list(map(int, input().split()))
s = sum(a)
n1 = a.count(1)
n2 = n - n1
b = ''
if(n2 != 0 and n1 != 0):
    b = '2 1 '
    n2 = n2 - 1
    n1 = n1 - 1
b = b + (n2) * '2 ' + (n1) * '1 '
print(b.strip())
