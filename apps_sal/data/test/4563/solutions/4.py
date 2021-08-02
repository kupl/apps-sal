t = 1
a = 1

for i in range(int(input())):
    T, A = map(int, input().split())
    n = max(-(-t // T), -(-a // A))
    t = n * T
    a = n * A

print(t + a)
