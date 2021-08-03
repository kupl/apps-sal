def read(): return list(map(int, input().split()))


t = int(input())
for i in range(t):
    a, b, c = read()
    print(a + b + c - 1)
