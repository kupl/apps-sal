N = int(input())
H = list(map(int, input().split()))
max_height = 0
count = 0
for h in H:
    if h >= max_height:
        max_height = h
        count += 1
print(count)
