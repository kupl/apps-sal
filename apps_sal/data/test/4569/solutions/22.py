S = input()
A = ['Sunny', 'Cloudy', 'Rainy']
c = A.index(S)
if c == 2:
    print(A[0])
else:
    print(A[c + 1])
