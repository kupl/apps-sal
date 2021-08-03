s, n, t = 0, int(input()), input()
print(sum(t[i - 3: i] in ['aaa', 'bbb'] for i in range((3 // n + 1) * n, len(t), n)))
