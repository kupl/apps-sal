'''
def main():
	from sys import stdin,stdout
def __starting_point():
	main()
'''
'''
def main():
	from sys import stdin,stdout
	N = int(stdin.readline())
	arr = list(map(int,stdin.readline().split()))
	div = []
	for i in arr:
		div.append(N//i)
	maxim = 0
	maxindex = -1
	for i in range(9):
		if div[i] >maxim:
			maxim = div[i]
			maxindex = i
	if maxindex > -1:
		ans = [ (maxindex+1) for i in range(maxim)]
		N= N%arr[maxindex]
		i = 0
		while i<maxim:
			for j in range(8,maxindex,-1):
				if arr[j]-arr[ans[i]-1] <=N:
					N -= arr[j]-arr[ans[i]-1]
					ans[i] = j+1
					break
			i+=1
		for i in ans:
			stdout.write(str(i))
	else:
		stdout.write('-1\n')
def __starting_point():
	main()
'''


def main():
    from sys import stdin, stdout
    import collections
    with open('input.txt', 'r') as ip:
        N, K = list(map(int, ip.readline().split()))
        arr = list(map(int, ip.readline().split()))
    mydict = collections.defaultdict(set)
    for i in range(len(arr)):
        mydict[arr[i]].add(i + 1)
    ans = []
    i = 0
    while K > 0:
        for it in mydict[sorted(list(mydict.keys()), reverse=True)[i]]:
            ans.append(it)
            K -= 1
            if K < 1:
                break
        minim = i
        i += 1
    with open('output.txt', 'w') as out:
        out.write(str(sorted(list(mydict.keys()), reverse=True)[minim]) + '\n')
        ans = ' '.join(str(x) for x in ans)
        out.write(ans + '\n')


def __starting_point():
    main()


__starting_point()
