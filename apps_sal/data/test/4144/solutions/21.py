N = int(input())
if N < 2:
    print(0)
else:
    print(((10**N - 9**N) * 2 - (10**N - 8**N)) % (10**9 + 7))
