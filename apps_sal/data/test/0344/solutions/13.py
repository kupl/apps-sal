r=input()
l=len(r)
vowel="aeiou"
for i in range(l-1):
	if r[i] not in vowel and r[i]!="n":
		if r[i+1] not in vowel:
			print ("NO")
			return
if r[-1] not in vowel and r[-1]!="n":
	print ("NO")
	return
print ("YES")
