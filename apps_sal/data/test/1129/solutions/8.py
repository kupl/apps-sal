n = int(input())
dots = [int(x) for x in input().split()]
dots.sort()
dot = dots[0]
left = 0
right = sum([abs(x - dot) for x in dots])
results = [right]
for i in range(1, n):
    ldot = dot
    dot = dots[i]
    left += (dot - ldot) * i
    right -= (dot - ldot) * (n - i)
    results.append(left + right)
print(dots[results.index(min(results))])

