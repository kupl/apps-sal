import heapq as h

n = int(input())
line2 = input().split()
a = []
for i in range(n):
    h.heappush(a,int(line2[i]))
if n == 1:
    print(0)
else:
    result = 0
    if n%2 == 1:
        k = n
    else:
        a.append(0)
        k = n + 1
    while k > 3:
        previous = h.heappop(a) + h.heappop(a)+ h.heappop(a)
        result += previous
        h.heappush(a, previous)
        k -= 2
    result += sum(a)
    print(result)
