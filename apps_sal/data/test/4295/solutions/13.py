N, K = map(int, input().split())
minCandidate1 = N % K
minCandidate2 = K - minCandidate1
if minCandidate1 <= minCandidate2:
    print(minCandidate1)
else:
    print(minCandidate2)
