a, b, t = list(map(int, input().split()))

time = 1
biscuit = 0

while time < t + 0.5:
    if time % a == 0:
        biscuit += b
    time += 1

print(biscuit)

