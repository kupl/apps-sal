(n, k) = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())
corr = input()
least = 0
for x in arr:
    if len(x) < len(corr):
        least += 1
lw = 0
for x in arr:
    if len(x) == len(corr):
        if x != corr:
            lw += 1
print(least // k * 5 + least + 1, (least + lw) // k * 5 + least + lw + 1)
