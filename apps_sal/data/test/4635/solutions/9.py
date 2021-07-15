q = int(input())

for i in range(q):
    n, k = map(int, input().split())
    t = ""
    for j in range(n):
        t += chr((j % k) + ord("a"))

    print(t)
