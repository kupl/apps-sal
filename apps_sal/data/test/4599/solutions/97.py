def solve1(n, lst):
    alice, bob = 0, 0

    for i in range(n):
        if i % 2 == 0:
            alice += lst[i]
        else:
            bob += lst[i]

    return alice - bob


n = int(input())
a = list(map(int, input().split(" ")))
a.sort(reverse=True)
print((solve1(n, a)))
