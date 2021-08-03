B = [0] * int(input())
for a in map(int, input().split()):
    B[a - 1] += 1
for b in B:
    print(b)
