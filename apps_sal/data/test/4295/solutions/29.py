from sys import stdin, stdout
for _ in range(1):  # int(stdin.readline())):
    # n=int(stdin.readline())
    n, k = list(map(int, stdin.readline().split()))
    if n % k == 0:
        print(0)
    else:
        rem = n % k
        print(min(rem, abs(k - rem)))
