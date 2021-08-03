import itertools
N = input()
digit = len(N)

N = int(N)


ans = 0
for i in range(1, digit + 1):
    for prod in itertools.product(("3", "5", "7"), repeat=i):
        if int("".join(prod)) <= N and len(set(prod)) == 3:
            ans += 1

print(ans)
