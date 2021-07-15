N = int(input())
A = list(map(int, input().split()))
 
sortA = sorted(set(A)) + [float('inf')]
 
def isOk(n):
    x = sortA[n]
    count = [0 for _ in range(2 * N + 1)]
    count[N + 1] = 1
 
    i = N + 1
    s = 1
    result = 0
 
    for a in A:
        if a >= x:
            i += 1
            s += count[i]
        else:
            s -= count[i]
            i -= 1
        result += s
        count[i] += 1
        s += 1
 
    if result >= N * (N + 1) // 4:
        return False
    else:
        return True
 
 
left = 0
right = len(sortA) - 1
 
while right - left > 1:
    mid = (left + right ) // 2
 
    if isOk(mid):
        right = mid
    else:
        left = mid
 
print(sortA[left])
