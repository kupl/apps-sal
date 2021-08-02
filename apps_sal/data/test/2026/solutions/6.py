M = int(input())
S = input()
anticmd = {
    'L': 'R',
    'R': 'L',
    'U': 'D',
    'D': 'U'
}
k = 0
stop = set()
for i in range(M):
    c = S[i]
    if c in stop:
        k += 1
        stop = set()

    stop.add(anticmd[c])

k += 1

print(k)
