(N, i) = map(int, input().split())
if N == 1:
    print(1)
elif N == 2:
    if i == 1:
        print(2)
    else:
        print(1)
else:
    print(N - i + 1)
