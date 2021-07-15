import sys
	
lines = sys.stdin.read().splitlines()


T, garb = list(map(int, lines[0].split()))

elim = list(map(int, lines[-1].split()))


common = []
other = []

for i in range(1,T+1):
	if i in elim:
		common.append(list(lines[i]))
	else:
		other.append(list(lines[i]))

res = "Yes"
leng = len(common[0])
word = common[0]
unwo = list("?"*leng)

for line in common:
	if len(line) == leng:
		word = [i if i == j else "?" for i, j in zip(line, word)]
	else:
		res = "No"
		break

for line in other:
	if len(line) == leng and [i if i == j else "?" for i, j in zip(line, word)] == word:
		res = "No"
		break
		
print(res)

if res == "Yes":
	print("".join(word))

