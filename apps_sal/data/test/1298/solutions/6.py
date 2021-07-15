_ = input()
s = input()

ans = 0
for i in range(len(s)):
	if s[i] == '1':
		ans += 1

	if s[i] == '0':
		ans -= 1

print(abs(ans))
