first = input().split()
n = first[0]
l = int(first[1])
second = input().split()
for i in range(len(second)):
    second[i] = int(second[i])
second.sort()
maximum = 0
for i in range(len(second)-1):
    current = second[i+1] - second[i]
    if current > maximum:
        maximum = current
maximum /= 2
if not 0 in second:
    current = second[0]
    if current > maximum:
        maximum = current
if not l in second:
    current = l - second[len(second)-1]
    if current > maximum:
        maximum = current
print("{:.10f}".format(maximum))
        

