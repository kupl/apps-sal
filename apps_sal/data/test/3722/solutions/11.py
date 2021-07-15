mod = 10 ** 9 + 7
n = int(input())
a, b, c, d = [input() for i in range(4)]
l = ["B", "A"]
if b == "A":
    b = l[not b == "A"]
    c = l[not c == "A"]
    a, d = l[not d == "A"], l[not a == "A"]
if n < 4:
    print(1)
elif d == "B":
    print(1)
elif c == "A":
    print(pow(2, n - 3, mod))
else:
    l = [1, 1]
    for i in range(n):
        l.append((l[-1] + l[-2]) % mod)
    print(l[n - 2]) 
