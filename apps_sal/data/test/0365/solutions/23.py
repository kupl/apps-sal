# your code goes here
segment, length = map(int, input().split(' '))
segments = [int(x) for x in input().strip().split(' ')]
total = sum(segments)
if total + segment - 1 == length:
    print("YES")
else:
    print("NO")
