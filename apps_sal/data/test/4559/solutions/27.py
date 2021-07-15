N = int(input())
A = list(map(int,input().split()))
result = 1
if 0 in A:
    print(0)
else:
    for i in A:
        result *= i
        if result > 10 ** 18:
            print("-1")
            break
    else:
        print(result)
