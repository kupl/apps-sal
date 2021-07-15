s = input()
oddc = {'a':0,'b':0}
evenc = {'a':0,'b':0}
odd = 0
even = 0
for i in range(len(s)):
	odd+=1
	if i%2 == 0:
		even += oddc[s[i]]
		odd += evenc[s[i]]
		evenc[s[i]]+=1
	else:
		even += evenc[s[i]]
		odd += oddc[s[i]]
		oddc[s[i]]+=1
print(str(even) + " " + str(odd))
