"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""
from sys import stdin, stdout


def main():
    (n, k) = [int(_) for _ in stdin.readline().strip().split()]
    s = stdin.readline().strip()
    last = dict()
    for i in range(26):
        c = chr(ord('A') + i)
        for j in range(n - 1, -1, -1):
            if s[j] == c:
                last[c] = j
                break
    guardAssigned = dict()
    for i in range(26):
        c = chr(ord('A') + i)
        guardAssigned[c] = False
    totalGuard = 0
    maxGuard = 0
    for (i, c) in enumerate(s):
        if not guardAssigned[c]:
            guardAssigned[c] = True
            totalGuard += 1
            maxGuard = max(maxGuard, totalGuard)
        if i == last[c]:
            totalGuard -= 1
    if maxGuard > k:
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')


def __starting_point():
    main()


__starting_point()
