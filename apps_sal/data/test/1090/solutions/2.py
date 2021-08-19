(n, k) = map(int, input().split())
s = input()
a = sum([s[i + 1] == s[i] for i in range(n - 1)])
print(min(a + 2 * k, n - 1))
