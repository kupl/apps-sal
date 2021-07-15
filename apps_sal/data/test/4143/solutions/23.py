n=int(input())
x = [int(input()) for _ in range(5)]
p = min(x)
q = n//p
if n % p == 0:
        print(q+4)
else:
        print(q+5)
