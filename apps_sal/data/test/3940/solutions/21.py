import sys
input = sys.stdin.readline

length, subs = list(map(int, input().strip().split()))
lol = 9999999999999999999999999999

for i in range(subs):
    start, end = list(map(int, input().strip().split()))
    if abs(start - end) + 1 < lol:
        lol = abs(start - end) + 1

print(lol)

construct = []
count = 0
while count < length:
    construct.append(str(count % lol))
    count += 1
print(' '.join(construct))
