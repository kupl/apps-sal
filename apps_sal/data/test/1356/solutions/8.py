s = input()
wyn = 0
for i in s:
	if i == "a":
		wyn += 1
print(min(len(s),2*wyn-1))
