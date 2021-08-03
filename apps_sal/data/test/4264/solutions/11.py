N = int(input())

kazu = 1
if N < 10:
    kazu = N
elif N < 100:
    kazu = 9
elif N < 1000:
    kazu = N - 90
elif N < 10000:
    kazu = 900 + 9
elif N < 100000:
    kazu = N - 9000 - 90
elif N == 100000:
    kazu = 90000 + 900 + 9

print(kazu)
