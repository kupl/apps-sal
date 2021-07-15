import sys;

c1, c2, c3, c4 = map(int, sys.stdin.readline().split(' '));
nbBuses, nbTrolleys = map(int, sys.stdin.readline().split(' '));

buses = map(int, sys.stdin.readline().split(' '));
trolleys = map(int, sys.stdin.readline().split(' '));

minBusesCost = 0;
for nbRide in buses:
	minBusesCost += min(c2, nbRide * c1);

minTrolleysCost = 0;
for nbRide in trolleys:
	minTrolleysCost += min(c2, nbRide * c1);

# print(c1, c2, c3, c4, minBusesCost, minTrolleysCost);

minCost = min(
	c4,
	min(
		c3,
		minBusesCost
	) +
	min(
		c3,
		minTrolleysCost
	)
);
print(minCost);
