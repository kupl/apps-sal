H, N = map(int, input().split())
List = list(map(int, input().split()))

Sum = sum(List)

if H <= Sum:
    print("Yes")
else:
    print("No")
