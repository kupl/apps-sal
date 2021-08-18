T = int(input())
n = [0] * T

for t in range(T):
    n, k = [int(i) for i in input().split(' ')]
    n1 = str(n)
    while n1.count('0') < 1 and k > 1:
        n += int(min(n1)) * int(max(n1))
        n1 = str(n)
        k -= 1
    print(n1)
