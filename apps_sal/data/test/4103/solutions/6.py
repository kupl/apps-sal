(n, b, a) = map(int, input().split())
path = map(int, input().split())
max_a = a
current_a = a
count = 0
for segment in path:
    if segment == 0:
        if current_a > 0:
            current_a -= 1
        else:
            b -= 1
    elif current_a == max_a or b == 0:
        current_a -= 1
    else:
        b -= 1
        current_a += 1
    count += 1
    if current_a == 0 and b == 0:
        break
print(count)
