T = int(input())
for i in range(T):
    (a, b) = map(int, input().split())
    k = len(str(b))
    print(a * (k - 1 + (b == 10 ** k - 1)))
