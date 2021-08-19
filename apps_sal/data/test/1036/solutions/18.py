def winner(x, y):
    return x if x + y in ['RS', 'PR', 'SP'] else y


(n, k) = list(map(int, input().split()))
s = input()
for _ in range(k):
    if len(s) % 2 == 1:
        s += s
    s = ''.join((winner(s[2 * i], s[2 * i + 1]) for i in range(len(s) // 2)))
print(s[0])
