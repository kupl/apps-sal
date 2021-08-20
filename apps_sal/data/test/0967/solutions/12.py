n = int(input())
a = [int(x) for x in input().split()]
answer = 0
last = a[-1]
for v in reversed(a):
    if v > last:
        break
    answer += 1
    last = v
print(len(a) - answer)
