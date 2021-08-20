N = int(input())
F = [int(''.join(input().split()), 2) for n in range(N)]
P = [list(map(int, input().split())) for n in range(N)]
print(max((sum((p[bin(n & f).count('1')] for (f, p) in zip(F, P))) for n in range(1, 1024))))
