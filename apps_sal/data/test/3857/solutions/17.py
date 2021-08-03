n = int(input())
ar = list(map(int, input().split()))
ar.sort()
stack = 0

chosen = [False] * n

for i in range(n):
    chosen[i] = False

for i in range(n):
    if(chosen[i] == False):
        chosen[i] = True
        stack += 1
        box = 1
        for j in range(i, n):
            if(chosen[j] == False and ar[j] >= box):
                chosen[j] = True
                box += 1

print(stack)
