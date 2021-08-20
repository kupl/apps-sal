score = 0
for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    if a != b:
        score += 2 * (a > b) - 1
if score == 0:
    print('Friendship is magic!^^')
elif score > 0:
    print('Mishka')
else:
    print('Chris')
