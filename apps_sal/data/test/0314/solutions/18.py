n, k = input().split()
n, k = int(n), int(k)
array = list(map(int, input().split()))

total = 0
saved = 0
found = False

for day in range(n):
    saved += array[day]
    
    given = min(saved, 8)
    total += given
    saved -= given

    if total >= k:
        found = True
        print(day+1)
        break
    
if not found:
    print(-1)

