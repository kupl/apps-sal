t = int(input())

for case in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    odd_wrong = 0
    even_wrong = 0

    for i, x in enumerate(a):
        if x % 2 == 0 and i % 2 == 1:
            even_wrong += 1

        if x % 2 == 1 and i % 2 == 0:
            odd_wrong += 1

    if odd_wrong == even_wrong:
        print(odd_wrong)
    else:
        print(-1)

