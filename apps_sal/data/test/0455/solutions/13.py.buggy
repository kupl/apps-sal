N = int(input())
Pi = []
for i in range(N):
    d = list(map(int, input().split()))
    Pi.append(d)

# validation
for p in Pi[1:]:
    if (p[0] + p[1]) % 2 != (Pi[0][0] + Pi[0][1]) % 2:
        print((-1))
        return

# create arms
Ai = []
if (Pi[0][0] + Pi[0][1]) % 2 == 0:
    Ai.append(1)
for i in range(0, 32):
    Ai.append(2 ** i)


def find_arm_pattern(arms, target_x, target_y):
    result = ""
    x = 0
    y = 0
    for a in arms:
        dx = target_x - x
        dy = target_y - y
        if abs(dx) >= abs(dy):
            if dx > 0:
                result += "R"
                x += a
            else:
                result += "L"
                x -= a
        else:
            if dy > 0:
                result += "U"
                y += a
            else:
                result += "D"
                y -= a
    if x == target_x and y == target_y:
        return result
    return None


arms = list(reversed(Ai))
results = []
for p in Pi:
    r = find_arm_pattern(arms, p[0], p[1])
    results.append(r)
txt = str(arms)
print((len(arms)))
print((txt[1:-1].replace(",", "")))
for r in results:
    print(r)
