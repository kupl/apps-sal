(n, k) = map(int, input().split())
s = input()
c = 'a' if s[k - 1] == 'A' else 'b' if s[k - 1] == 'B' else 'c'
print(s[:k - 1] + c + s[k:])
