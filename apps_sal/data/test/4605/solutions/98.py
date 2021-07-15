N,A,B = map(int, input().split())
result = 0

def FindSomeOfDegit(x):
    count = 0
    while x > 0:
        count += x%10 
        x = x // 10
    return count

for i in range(N+1):
    count = FindSomeOfDegit(i)
    if A <= count <= B:
        result += i

print(result)
