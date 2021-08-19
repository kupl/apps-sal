from sys import stdin, stdout
for _ in range(1):  # int(stdin.readline())):
    # n=int(stdin.readline())
    # a=list(map(int,stdin.readline().split()))
    s = len(set(input()))
    print('Yes' if s > 1 else 'No')
