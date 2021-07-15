s, shift = 'qwertyuiopasdfghjkl;zxcvbnm,./', (1 if input().strip() == 'R' else -1)
print(''.join(s[s.find(c) - shift] for c in input().strip()))

