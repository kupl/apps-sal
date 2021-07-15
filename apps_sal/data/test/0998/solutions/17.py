n, x = map(int, input().split())
if x>=2**n:
    prefix_array = []
    for i in range(1, 2**n):
        prefix_array.append(i)
else:
    prefix_array = []
    compl = {}
    for i in range(1, 2**n):
        if i==x: continue
        try:
            if compl[i]: pass
        except:
            prefix_array.append(i)
            compl[i^x] = True
if prefix_array==[]: print(0)
else:
    res = [prefix_array[0]]
    for i in range(len(prefix_array)-1):
        res.append(prefix_array[i]^prefix_array[i+1])
    print(len(res))
    for i in res: print(i, end=' ')
    print()

