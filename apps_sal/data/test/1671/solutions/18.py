import math
n = int(input())
m = input().split()
end = []
for i in range(len(m)):
    m[i] = int(m[i])
min_req = math.floor(sum(m) / len(m))
remainder = sum(m) % len(m)
m.sort()
for i in range(len(m)):
    end.append(min_req)
for i in range(remainder):
    end[i] += 1
end.sort()
counter = 0
for i in range(len(m)):
    counter += abs(m[i] - end[i])
counter /= 2
print(int(counter))
