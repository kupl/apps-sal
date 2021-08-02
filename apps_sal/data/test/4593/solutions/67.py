x = int(input())
max_val = 1
for i in range(1, x):
    for j in range(2, x):
        val = i ** j
        if val > x:
            break
        elif val > max_val:
            max_val = val
print(max_val)
