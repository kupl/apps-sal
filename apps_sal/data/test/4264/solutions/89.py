N = int(input())
if N < 10:
    print(N)
elif 10 <= N and N < 100:
    print(9)
elif 100 <= N and N < 1000:
    print(9 + (N - 100 + 1))
elif 1000 <= N and N < 10000:
    print(909)
elif 10000 <= N and N < 100000:
    print(909 + (N - 10000 + 1))
else:
    print(90909)
