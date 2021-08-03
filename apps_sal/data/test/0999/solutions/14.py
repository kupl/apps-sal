n1 = int(input())

start1, end1 = list(map(int, input().split()))

n1 -= 1

for _ in range(n1):
    s1, e1 = list(map(int, input().split()))
    if s1 > start1:
        start1 = s1
    if e1 < end1:
        end1 = e1

n2 = int(input())

start2, end2 = list(map(int, input().split()))

n2 -= 1

for _ in range(n2):
    s2, e2 = list(map(int, input().split()))
    if s2 > start2:
        start2 = s2
    if e2 < end2:
        end2 = e2

gap = max(0, start2 - end1, start1 - end2)
print(gap)
