n = int(input())
V = 2 ** (n + 1) - 1
lights = [0] * (V + 1)
rem_lights = [0] * (V + 1)
for i,v in enumerate(input().split()):
    lights[i + 2] = int(v)
stack = [3,2]
while(stack):
    i = stack.pop()
    rem_lights[i] = rem_lights[i // 2] + lights[i]
    if (2 * i < V):
        stack.append(2 * i + 1)
        stack.append(2 * i)
m = max(rem_lights)
#print("max:"+str(m))
#print(rem_lights)
for i in range(2 ** n,2 ** (n + 1) - 1,2):
        rem_lights[i] = m - rem_lights[i]
        rem_lights[i + 1] = m - rem_lights[i + 1]
while n:
    for i in range(2 ** n,2 ** (n + 1) - 1,2):
        small = min(rem_lights[i],rem_lights[i + 1])
        rem_lights[i // 2] = small
        rem_lights[i] -= small
        rem_lights[i + 1] -= small
    n-=1
#print(rem_lights)
print(sum(rem_lights))
