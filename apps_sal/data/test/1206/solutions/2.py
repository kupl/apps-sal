import itertools

n = int(input())
pairs = []
for i in range(n):
    pairs.append([int(x) for x in input().split()])
allPairs = [x for x in (itertools.product((0, 1, 2), repeat=len(pairs))) if (x.count(0) == 1 and x.count(1) >= 1) or (x.count(0) == 0 and x.count(1) >= 2)]


def analyze_sec_price_prob(companiesProb):
    secPriceProb = 0
#	print(companiesProb, "||||||||||")
    for oneChoice in allPairs:
        compChain = 1
        for index in range(len(companiesProb)):
            compChain *= companiesProb[index][oneChoice[index]]
        secPriceProb += compChain
#		if compChain > 0:
#			print(oneChoice, "&&&&&&&&&")
    return secPriceProb


def math_exp_sec(pairs):
    result = 0
    for secondPrice in range(1, 10001):
        curProb = []
        for limit in pairs:
            if secondPrice < limit[0]:
                secondPriceLess = 1
                secondPriceEq = 0
                secondPriceBig = 0
            elif limit[0] <= secondPrice <= limit[1]:
                secondPriceLess = (limit[1] - secondPrice) / (limit[1] - limit[0] + 1.0)
                secondPriceEq = 1.0 / (limit[1] - limit[0] + 1.0)
                secondPriceBig = (secondPrice - limit[0]) / (limit[1] - limit[0] + 1.0)
            else:
                secondPriceLess = 0
                secondPriceEq = 0
                secondPriceBig = 1
            curProb.append((secondPriceLess, secondPriceEq, secondPriceBig))
        result += secondPrice * analyze_sec_price_prob(curProb)
    return result


print(math_exp_sec(pairs))
