N = int(input())
A = list(map(int, input().split()))
B = list(map(abs, A))
print(sum(B) - 2 * min(B) * (sum(a < 0 for a in A) % 2))
