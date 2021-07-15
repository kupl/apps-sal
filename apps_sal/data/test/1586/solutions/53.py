N = int(input())
i = 2
a = 0
while i <= N:
    a += N // i
    i *= 2
i = 2*5
b = 0
while i <= N:
    b += N // i
    i *= 5
print(min(a,b) if N % 2 == 0 else 0)
