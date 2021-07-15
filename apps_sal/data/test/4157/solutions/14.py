n = int(input())
inputlist = list(map(int,input().split()))
outputlist = [inputlist.pop(0)]
while len(inputlist) > 0:
	for i in range(len(inputlist)):
		if outputlist[0]*3 == inputlist[i]:
			outputlist = [inputlist.pop(i)] + outputlist
			break
		elif inputlist[i]*3 == outputlist[-1]:
			outputlist = outputlist + [inputlist.pop(i)]
			break
		elif outputlist[-1]*2 == inputlist[i]:
			outputlist = outputlist + [inputlist.pop(i)]
			break
		elif inputlist[i]*2 == outputlist[0]:
			outputlist = [inputlist.pop(i)] + outputlist 
			break
print(' '.join(list(map(str,outputlist))))
