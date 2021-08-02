N = int(input())
judge = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

for _ in range(N):
    j_input = input()
    for j in judge.keys():
        if j_input == j:
            judge[j] += 1

for j in judge.keys():
    print(j, end=" x ")
    print(judge[j])
