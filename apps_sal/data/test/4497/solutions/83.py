from itertools import count
n = int(input())
for i in count(0):
    if n < 2**(i + 1):
        print(2**i)
        break
