import sys
input = sys.stdin.readline
n = int(input())
evens = []
odds = []
for i in map(int, input().split()):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
evens.sort(reverse=True)
odds.sort(reverse=True)
if len(evens) > len(odds):
    print(sum(evens[len(odds) + 1:]))
elif len(odds) > len(evens):
    print(sum(odds[len(evens) + 1:]))
else:
    print(0)
