t = int(input())
for _ in range(t):
    a = int(input())
    print(2**(str(bin(a)).count('1')))
