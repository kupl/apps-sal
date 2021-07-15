N = int(input())
string = ["AC", "WA", "TLE", "RE"]
count = [0] * 4
for i in range(N):
    s = input()
    if s == "AC":
        count[0] = count[0] + 1
    elif s == "WA":
        count[1] = count[1] + 1
    elif s == "TLE":
        count[2] = count[2] + 1
    else:
        count[3] = count[3] + 1
for j in range(len(count)):
    print(string[j] + " x " + str(count[j]))
