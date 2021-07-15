n = int(input())
a = list(map(int, input().split()))

left = [0]*n
for i, el in enumerate(a):
    if i == 0:
        left[i] = int(el < 0)
    else:
        left[i] = left[i-1] + int(el < 0)

l_count = [0]*n
for i, el in enumerate(left):
    if i == 0:
        l_count[i] = 1
    else:
        l_count[i] = l_count[i-1] + int(left[i-1]%2 == 0)

neg_count = 0
for r in range(n):
    if left[r]%2 == 1:
        neg_count += l_count[r]
    else:
        neg_count += r+1 - l_count[r]

pos_count = n*(n+1)//2 - neg_count

print(neg_count, pos_count)
