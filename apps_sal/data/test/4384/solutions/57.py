N = int(input())
if 1 <= N < 1000:
    print('ABC')
elif 1000 <= N < 1999:
    print('ABD')
elif N <= 0 or 1999 <= N:
    print('Out of range')
