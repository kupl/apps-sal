N = int(input())
l = [int(input()) for _ in range(N)]
largest = max(l)
largest_index = l.index(max(l))
second_largest = sorted(l)[-2]
second_largest_index = l.index(second_largest)

for idx, n in enumerate(l):
    if idx == largest_index:
        print(second_largest)
    else:
        print(largest)
