N = int(input())
count = [0, 0, 0, 0]
for _ in range(N):
    word = input()
    if word == 'AC':
        count[0] += 1
    elif word == 'WA':
        count[1] += 1
    elif word == 'TLE':
        count[2] += 1
    elif word == 'RE':
        count[3] += 1
print('AC x ', count[0])
print('WA x ', count[1])
print('TLE x ', count[2])
print('RE x ', count[3])
