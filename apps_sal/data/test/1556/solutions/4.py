import heapq
s = input().split()
n = int(s[0])
k = int(s[1])
x = int(s[2])
neg = 0
zeroes = 0
numbers = list(map(int, input().split()))
num = []
for i in numbers:
    if(i < 0):
        neg += 1
    elif(i == 0):
        zeroes += 1

for i, x1 in enumerate(numbers):
    num.append([abs(x1), i])
heapq.heapify(num)
temp = []
steps = 0
if(neg % 2 == 0):
    temp = heapq.heappop(num)
    # print(temp[1],temp[0])
    # print(numbers[temp[1]],x)
    if(numbers[temp[1]] < 0):
        steps = min(abs(numbers[temp[1]]) // x + 1, k)
        k -= steps
        numbers[temp[1]] += steps * x
        heapq.heappush(num, [abs(numbers[temp[1]]), temp[1]])
    else:
        steps = min((abs(numbers[temp[1]]) // x) + 1, k)
        # print(steps)
        k -= steps
        numbers[temp[1]] -= steps * x
        heapq.heappush(num, [abs(numbers[temp[1]]), temp[1]])

while(k > 0):
    temp = heapq.heappop(num)
    # print(temp[1],temp[0])
    if(numbers[temp[1]] < 0):
        # steps = (numbers[temp[1]]//x+1)
        # k-=steps
        numbers[temp[1]] -= x
        heapq.heappush(num, [abs(numbers[temp[1]]), temp[1]])
    else:
        # steps = (numbers[temp[1]]//x+1)
        # k-=steps
        numbers[temp[1]] += x
        heapq.heappush(num, [abs(numbers[temp[1]]), temp[1]])
    k -= 1
for i in numbers:
    print(i, end=" ")
