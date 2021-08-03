N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

i = 1
while i <= K:
    i *= 2

x = 0
while i != 0:
    if sum([1 for a in A if a & i == 0]) > N / 2:
        if x + i <= K:
            x += i
    i //= 2

print((sum([a ^ x for a in A])))
