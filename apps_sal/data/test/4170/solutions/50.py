n = int(input())
h = [int(s) for s in input().split()]

max_val = 0
temp = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        temp += 1
        if temp > max_val:
            max_val = temp
    else:
        temp = 0
print(max_val)
