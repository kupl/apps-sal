import sys

input = sys.stdin.readline
S = input()
S = S.replace('\n' , '')
tmp = ""
division_count = 0
for s in S:
    if tmp == "":
        tmp = s
        continue
    if tmp == s:
        continue
    else:
        tmp = s
        division_count += 1
print(division_count)
