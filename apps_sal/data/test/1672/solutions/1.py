#Magnets

n = int(input())

groups = 0
last_magnet = ""
last_magnet = input()
groups += 1
for i in range(n-1):
	magnet = input()
	if magnet != last_magnet:
		groups += 1
	last_magnet = magnet
print(groups)
