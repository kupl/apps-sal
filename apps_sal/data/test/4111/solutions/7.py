n = int(input())
arr = [int(x) for x in input().split()]
evens = [0]
odds = [0]
for i in range(len(arr)):
    if i % 2 == 0:
        evens.append(evens[-1] + arr[i])
    else:
        odds.append(odds[-1] + arr[i])
evens += [evens[-1]]
odds += [odds[-1]]
cnt = 0
for i in range(len(arr)):
    if i % 2 == 0:
        if evens[i//2] + (odds[-1] - odds[i//2]) == odds[i//2] + (evens[-1] - evens[i//2 + 1]):
            cnt += 1
    else:
        if evens[i//2 + 1] + (odds[-1] - odds[i//2 + 1]) == odds[i//2] + (evens[-1] - evens[i//2 + 1]):
            cnt += 1        
print(cnt)
