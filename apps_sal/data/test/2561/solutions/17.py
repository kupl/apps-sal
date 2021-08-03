n = int(input())
for _ in range(n):
    a = int(input())
    print(2 ** bin(a).count("1"))
