n, d = list(map(int, input().split()))

max_stroke = 0
current_stroke = 0

for i in range(d):
    schedule = input()
    if '0' in schedule:
        current_stroke += 1
        if current_stroke > max_stroke:
            max_stroke = current_stroke
    else:
        current_stroke = 0

print(max_stroke)
