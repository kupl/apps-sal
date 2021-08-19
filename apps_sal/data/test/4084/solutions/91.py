(n, a, b) = map(int, input().split())
i = a + b
div = n // i
rm = n % i
print(div * a + min(rm, a))
