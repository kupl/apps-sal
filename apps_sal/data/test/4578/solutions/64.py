(a, b) = map(int, input().split())
c = [int(input()) for i in range(a)]
print(a + (b - sum(c)) // min(c))
