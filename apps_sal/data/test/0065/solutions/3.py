n = int(input())

a = list(map(int, input().strip().split()))

x = min(a)

best = 10**6
last = None
i = 0
while i < len(a):
    if a[i] == x:
        if last is None:
            last = i
        else:
            razlika = i - last
            best = min(razlika, best)
            last = i
    i += 1
print(best)

