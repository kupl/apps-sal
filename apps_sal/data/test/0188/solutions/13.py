import heapq
rows, groups = list(map(int, input().split()))
counts = list([(-1) * int(x) for x in input().split()])

fours = rows
twos = 2 * rows
ones = 0

f = True
heapq.heapify(counts)
while fours + twos + ones > 0 and len(counts) > 0:
    i = heapq.heappop(counts)
    i = i * (-1)
    if fours >= 1:
        if i < 4:
            twos += fours
            ones += fours
            fours = 0
            heapq.heappush(counts, i * (-1))
        else:
            d, m = divmod(i, 4)
            if d > fours:
                i -= fours * 4
                fours = 0
                if i > 0:
                    heapq.heappush(counts, i * (-1))
            else:
                i -= d * 4
                fours -= d
                if i > 0:
                    heapq.heappush(counts, i * (-1))
    elif twos >= 1:
        if i < 2:
            ones += twos
            twos = 0
            heapq.heappush(counts, i * (-1))
        else:
            d, m = divmod(i, 2)
            if d > twos:
                i -= twos * 2
                twos = 0
                if i > 0:
                    heapq.heappush(counts, i * (-1))
            else:
                i -= d * 2
                twos -= d
                if i > 0:
                    heapq.heappush(counts, i * (-1))
    elif ones >= 1:
        if i > ones:
            f = False
            break
        else:
            ones -= i
if len(counts) > 0 or f == False:
    print("NO")
else:
    print("YES")
