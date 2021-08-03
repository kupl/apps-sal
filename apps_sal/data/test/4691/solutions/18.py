N = int(input())
result = ["AC", "WA", "TLE", "RE"]
S = [input() for i in range(N)]

for i in result:
    print(i, "x", S.count(i))
