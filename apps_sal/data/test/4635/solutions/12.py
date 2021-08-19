s = ''
for i in range(ord('a'), ord('z') + 1):
    s += chr(i)
for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    print(s[:k] * (n // k) + s[:n % k])
