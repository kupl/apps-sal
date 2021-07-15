with open(0) as f:
    N,  *S = map(int, f.read().split())
Score = [True if i == 0 else False for i in range(10000)]
for s in S:
    for i in reversed(range(s, 10000)):
        if Score[i-s]:
            Score[i] = True

for i in reversed(range(10000)):
    if Score[i] and i % 10 != 0:
        print(i)
        break
else:
    print(0)
