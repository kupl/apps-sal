n = int(input())
s = list(map(str, input()))
ans = [chr((ord(s[i]) - ord('A') + n) % 26 + ord('A')) for i in range(len(s))]
print(''.join(ans))
