n,b,a = map(int, input().split())

s = list(map(int, input().split()))

cb, ca = b, a

i = 0

while (cb or ca) and i < len(s):

	if s[i] == 1:

		if ca < a:
			if cb:

				cb -= 1

				ca += 1

			else:
				ca -= 1
		else:

			ca -= 1

	else:

		if ca:

			ca -= 1

		else:

			cb -= 1

	i += 1

print(i)
