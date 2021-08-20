from collections import Counter
import sys
n = int(input())
colors = list(map(int, sys.stdin.readline().split()))
total = 0
freqs = {colors[0]: 1}
freqs_of_freqs = {1: 1}
max_length = 1
for (index, color) in enumerate(colors[1:]):
    if color not in freqs:
        freqs[color] = 1
        freqs_of_freqs[1] = freqs_of_freqs.get(1, 0) + 1
    else:
        freqs_of_freqs[freqs[color]] -= 1
        if freqs_of_freqs[freqs[color]] == 0:
            del freqs_of_freqs[freqs[color]]
        freqs[color] += 1
        freqs_of_freqs[freqs[color]] = freqs_of_freqs.get(freqs[color], 0) + 1
    if len(freqs_of_freqs) == 2:
        l = list(freqs_of_freqs.keys())
        if max(l) == min(l) + 1 and freqs_of_freqs[max(l)] == 1:
            max_length = index + 2
        elif 1 in list(freqs_of_freqs.keys()) and freqs_of_freqs[1] == 1:
            max_length = index + 2
    elif len(freqs_of_freqs) == 1:
        if 1 in list(freqs_of_freqs.keys()) or 1 in list(freqs_of_freqs.values()):
            max_length = index + 2
print(max_length)
