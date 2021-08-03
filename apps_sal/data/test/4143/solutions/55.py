n = int(input())
time = [int(input()) for _ in range(5)]
count = 0
if all([i >= n for i in time]):
    print((5))
else:
    smallest = min(time)
    smallest_index = time.index(smallest)
    count += n // smallest
    if n % smallest != 0:
        count += 1
    print((count + 4))
