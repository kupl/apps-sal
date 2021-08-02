n = int(input())

s = list(map(int, input().strip().split()))

s = sorted(s)

mean = sum(s) / len(s)

l = 0
while mean < 4.5:
    s[l] = 5
    l += 1
    mean = sum(s) / len(s)

print(l)
