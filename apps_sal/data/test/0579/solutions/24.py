import numpy as np

def __starting_point():
	N,K = list(map(int,input().split()))
	P = [ int(p)-1 for p in input().split() ]
	C = list(map(int,input().split()))
	cycleIDs = np.full( N, -1, np.int64 )
	cycleInfs = []
	cycleID = 0
	procCnt = 0
	for n in range(N):
		v = n
		if cycleIDs[v] != -1:
			continue
		else:
			currentCycleCosts = []
			while True:
				currentCycleCosts.append( C[v] )
				cycleIDs[v] = cycleID

				v = P[v]
				if cycleIDs[v] != -1:
					procCnt = K % len( currentCycleCosts )
					if len( currentCycleCosts ) + procCnt <= K:
						procCnt += len( currentCycleCosts )
					cycleInfs.append( ( procCnt, len(currentCycleCosts), np.array( currentCycleCosts + currentCycleCosts ) ) )
					cycleID += 1
					break
	ans = -10 ** 9
	for procCnt, currentCycleSize, currentCycleCosts in cycleInfs:
		loopScore = 0
		if np.sum(currentCycleCosts) > 0:
			cycleLoopCnt =  ( K - procCnt ) // currentCycleSize
			loopScore = cycleLoopCnt * np.sum(currentCycleCosts[:currentCycleSize])

		for i in range(currentCycleSize):
			ans = max( ans, np.roll( currentCycleCosts, i ).cumsum()[:procCnt].max() + loopScore )

	print(ans)

__starting_point()
