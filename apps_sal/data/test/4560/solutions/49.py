N = int(input())
A = int(input())

Amari = N % 500

if A >= Amari:
    print('Yes')

elif A < Amari:
    print('No')
