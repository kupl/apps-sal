n = int(input())
if ord(str(n)[-1]) > ord('5'):
    print(n + 10 - ord(str(n)[-1]) + ord('0'))
else:
    print(n - ord(str(n)[-1]) + ord('0'))

