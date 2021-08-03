N = int(input())
A = list(map(int, input().split()))

B = list(set(A))

if len(B) % 2 == 0:
    print((len(B) - 1))
else:
    print((len(B)))
