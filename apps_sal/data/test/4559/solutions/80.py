N = int(input())
A=list(map(int, input().split()))

const = 10**18

if 0 in A:
    print(0)
    return

result = 1
for i in A:
    result *= i
    if result>const:
        print(-1)
        return
print(result)
