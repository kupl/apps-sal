n, k = map(int, input().split())
s = input()
print(min(sum([1 for i in range(n - 1) if s[i] == s[i + 1]]) + k * 2, n - 1))
