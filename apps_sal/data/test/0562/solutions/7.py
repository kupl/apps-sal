n = int(input())
segment = []

for _ in range(n):
    segment.append(list(map(int, input().split())))

segment.sort(key=lambda x: x[0])

start1 = 0
end1 = -float('inf')
start2 = 0
end2 = -float('inf')

for x in segment:
    start = x[0]
    end = x[1]

    if start > end1:
        start1 = start
        end1 = end
    elif start > end2:
        start2 = start
        end2 = end
    else:
        print("NO")
        return

print("YES")
