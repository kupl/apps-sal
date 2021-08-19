import sys
n = int(sys.stdin.readline().rstrip())
locations = {'R': [], 'G': [], 'B': []}
for i in range(n):
    (x, c) = sys.stdin.readline().rstrip().split()
    locations[c].append(int(x))


def solve(locations):
    count = 0
    rPtr = 0
    bPtr = 0
    gPtr = 0
    if len(locations['G']) == 0:
        if len(locations['R']):
            count += locations['R'][-1] - locations['R'][0]
        if len(locations['B']):
            count += locations['B'][-1] - locations['B'][0]
        return count
    while len(locations['G']) > gPtr:
        if len(locations['R']) > rPtr and locations['G'][gPtr] > locations['R'][rPtr]:
            count += locations['G'][gPtr] - locations['R'][rPtr]
            while len(locations['R']) > rPtr and locations['G'][gPtr] > locations['R'][rPtr]:
                rPtr += 1
        if len(locations['B']) > bPtr and locations['G'][gPtr] > locations['B'][bPtr]:
            count += locations['G'][gPtr] - locations['B'][bPtr]
            while len(locations['B']) > bPtr and locations['G'][gPtr] > locations['B'][bPtr]:
                bPtr += 1
        if len(locations['G']) == gPtr + 1:
            if len(locations['R']) > rPtr:
                count += locations['R'][-1] - locations['G'][gPtr]
            if len(locations['B']) > bPtr:
                count += locations['B'][-1] - locations['G'][gPtr]
            return count
        if len(locations['G']) > gPtr + 1:
            prevR = locations['G'][gPtr]
            maxRd = 0
            while len(locations['R']) > rPtr:
                if locations['R'][rPtr] < locations['G'][gPtr + 1]:
                    maxRd = max(maxRd, locations['R'][rPtr] - prevR)
                    prevR = locations['R'][rPtr]
                    rPtr += 1
                else:
                    break
            maxRd = max(maxRd, locations['G'][gPtr + 1] - prevR)
            prevB = locations['G'][gPtr]
            maxBd = 0
            while len(locations['B']) > bPtr:
                if locations['B'][bPtr] < locations['G'][gPtr + 1]:
                    maxBd = max(maxBd, locations['B'][bPtr] - prevB)
                    prevB = locations['B'][bPtr]
                    bPtr += 1
                else:
                    break
            maxBd = max(maxBd, locations['G'][gPtr + 1] - prevB)
            count += min(2 * (locations['G'][gPtr + 1] - locations['G'][gPtr]), 3 * (locations['G'][gPtr + 1] - locations['G'][gPtr]) - maxRd - maxBd)
            gPtr += 1
    return count


print(solve(locations))
