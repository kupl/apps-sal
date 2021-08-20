n = int(input())
A = [a for a in input().split(' ')]
if n == 1:
    print(A[0])
else:
    odd = A[::2]
    even = A[1::2]
    if n % 2 == 0:
        even.reverse()
        print(' '.join(even + odd))
    else:
        odd.reverse()
        print(' '.join(odd + even))
