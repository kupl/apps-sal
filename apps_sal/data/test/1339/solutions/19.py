n = int(input())
ret = -1
left = []
right = []

for i in range(n):
    a, b = map(int, input().split(" "))
    left.append(a)
    right.append(b)
ml = left[0]
mr = right[0]
for i in range(n):
    if(left[i] < ml):
        ml = left[i]
    if(right[i] > mr):
        mr = right[i]
for i in range(n):
    if(left[i] <= ml and mr <= right[i]):
        ret = i + 1
print(ret)
