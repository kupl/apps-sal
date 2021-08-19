N = int(input())
a = []
for i in range(N):
    a.append(int(input()) - 1)
flag = True
step = []
pivot = 0
for i in range(N + 1):
    step.append(pivot)
    if a[pivot] == 1:
        break
    pivot = a[pivot]
if len(step) > N:
    print(-1)
else:
    print(len(step))
