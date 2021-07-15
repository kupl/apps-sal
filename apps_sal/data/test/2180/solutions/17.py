n = int(input())
s = "C." * n
print((n * n + 1) // 2)
print('\n'.join(s[i:n + i] for i in range(n)))
