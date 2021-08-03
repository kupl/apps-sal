N = int(input())

M = 10**9 + 7

a = 10**N % M
b = 2 * (9**N) % M
c = 8**N % M

print((a - b + c) % M)
