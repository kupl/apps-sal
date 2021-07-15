import math

mod= 1000000007

x, y = [int(x) for x in input().split()]

if y%x != 0:
    print(0)
    return
 
y= y//x
seqs=set()	

for x in range(1, int(math.sqrt(y) + 1)):
	if y%x != 0:
		continue
	seqs.add(x)
	seqs.add(y// x)

seqs=sorted(list(seqs))
ordered= seqs.copy()

for i in range(len(seqs)):
	ordered[i]=pow(2, seqs[i] - 1, mod)
	for j in range(i):
		if seqs[i]% seqs[j] == 0:
			ordered[i]-= ordered[j]
print(int(ordered[len(ordered)-1] % mod))

