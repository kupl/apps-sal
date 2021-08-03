def read(): return map(int, input().split())


t = int(input())
for i in range(t):
    a, b = read()
    print(a ^ b)
