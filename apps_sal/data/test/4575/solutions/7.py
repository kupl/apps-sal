n = int(input())
d, x = list(map(int, input().split()))

choco = []
while True:
	try:
		choco.append(int(input()))
	except EOFError:
		break

choco = [i * x + 1 for i in range(d) for x in choco if i * x + 1 <= d]

print((x + len(choco)))

