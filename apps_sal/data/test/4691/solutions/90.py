# listじゃなくてdict使いたい
n = int(input())
j = [0] * 4
moji = ["AC", "WA", "TLE", "RE"]
for i in range(n):
    s = input()
    if s == "AC":
        j[0] += 1
    elif s == "WA":
        j[1] += 1
    elif s == "TLE":
        j[2] += 1
    elif s == "RE":
        j[3] += 1
for k in range(4):
    print(f"{moji[k]} x {j[k]}")
