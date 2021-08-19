S = input()
(lower, upper, number) = (False, False, False)
(L, U, N) = ([str(i) for i in range(10)], [chr(i) for i in range(ord('A'), ord('Z') + 1)], [chr(i) for i in range(ord('a'), ord('z') + 1)])
for letter in S:
    lower = lower or letter in L
    upper = upper or letter in U
    number = number or letter in N
if len(S) >= 5 and lower and upper and number:
    print('Correct')
else:
    print('Too weak')
