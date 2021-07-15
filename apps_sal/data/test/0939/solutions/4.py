import sys;

nbDancers, nbDances = list(map(int, sys.stdin.readline().split(' ')));
dancers = [0]*(nbDancers+1);

for line in sys.stdin:
	taken = [False, False, False, False];

	ds = list(map(int, line.split(' ')));

	for d in ds:
		taken[dancers[d]] = True;

	for d in ds:
		if dancers[d] == 0:
			iCurr = 1;
			while iCurr <= 3 and taken[iCurr]:
				iCurr += 1;

			dancers[d] = iCurr;
			taken[iCurr] = True;

print((' '.join(map(str, dancers[1:]))));

