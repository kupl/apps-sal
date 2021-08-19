n = int(input())
odd = 0
lowest_odd = None
s = 0
for num in map(int, input().split()):
    s += num
    if num % 2 == 1:
        odd += 1
        if lowest_odd is None or num < lowest_odd:
            lowest_odd = num
if odd % 2 == 1:
    print(s - lowest_odd)
else:
    print(s)
