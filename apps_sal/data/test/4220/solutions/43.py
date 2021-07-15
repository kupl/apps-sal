n = int(input())
if n < 1 or n > 100:
    return

n1 = input()

i = len(n1)
if i < 1 or i > 100:
    return

n2 = '...'

if n >= i:
    print(n1)
else:
    print(n1[:n] + n2)
