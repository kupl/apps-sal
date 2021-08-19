n = int(input())
a = list(map(int, input().split()))
even = [a[i] for i in range(1, n, 2)]
odd = [a[i] for i in range(0, n, 2)]
if n % 2 == 0:
    print(*even[::-1] + odd)
else:
    print(*odd[::-1] + even)
